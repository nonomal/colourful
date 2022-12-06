<template>
  <div class="common-layout">
    <h1>百度云自动补档</h1>

    <el-row>
      <el-col>
        <el-table
          stripe
          :data="shareList.slice((page - 1) * pageSize, page * pageSize)"
        >
          <el-table-column label="分享ID(点击打开自动分享链接)">
            <template v-slot="scope">
              <el-link :href="'/api/reshare/' + scope.row.shareId" type="primary" target="_blank">{{scope.row.shareId}}</el-link>
            </template>
          </el-table-column>
          <el-table-column label="分享文件" prop="typicalPath" />
          <el-table-column label="分享时间" :formatter="formatTimestamp" />
          <el-table-column
            label="状态"
            prop="expiredType"
            :formatter="formatExpiredType"
          />
          <el-table-column
            label="文件id"
            prop="fsIds"
            :formatter="formatFsIds"
          />
          <el-table-column label="浏览次数" prop="vCnt" />
          <el-table-column label="操作" min-width="120px">
            <template v-slot="scope">
              <el-button
                type="primary"
                size="small"
                @click="reshare(scope.row.shareId)"
                >重新分享</el-button
              >
              <el-button
                type="danger"
                size="small"
                @click="cancelShare(scope.row.shareId)"
                >取消分享</el-button
              >
              <el-button
                type="success"
                size="small"
                @click="copyLink(scope.row)"
                >复制链接</el-button
              >
            </template>
          </el-table-column>
        </el-table>
        <div style="display: flex; justify-content: flex-end">
          <el-pagination
            :current-page="page"
            :page-sizes="[15, 50, 100, 300]"
            :page-size="pageSize"
            :total="shareList.length"
            layout="total, sizes, prev, pager, next, jumper"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
          ></el-pagination>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      shareList: [],
      page: 1,
      pageSize: 15,
    };
  },

  mounted() {
    this.getShareList();
  },
  methods: {
    handleSizeChange(val) {
      this.page = 1;
      this.pageSize = val;
    },
    handleCurrentChange(val) {
      this.page = val;
    },
    formatTimestamp(row) {
      return this.moment(row.ctime * 1000).format("YYYY-MM-DD HH:mm:ss");
    },
    formatFsIds(row) {
      return row.fsIds.join(",");
    },
    formatExpiredType(row) {
      const shareStatusMap = {
        1: "分享失败",
        2: "暂时不可访问",
        3: "分享失败",
        4: "审核未通过",
        19: "已被冻结",
      };
      const shareTagMap = {
        7: "已屏蔽",
      };

      var e = row.expiredType,
        n = row.expiredTime,
        i = row.status,
        a = row.tag,
        s = ["已失效", "有效期内", "永久有效"],
        r = "-";
      return shareStatusMap[i]
        ? (r = shareStatusMap[i])
        : shareTagMap[a]
        ? (r = shareStatusMap[a])
        : 0 === +e
        ? (r = this.getValidTime(+n))
        : +e >= -1 && +e <= 1 && (r = s[+e + 1]);
    },
    getValidTime(t) {
      var e = +t;
      if (e > 0) {
        for (
          var n = [
              {
                time: 86400,
                desc: "天",
              },
              {
                time: 3600,
                desc: "小时",
              },
              {
                time: 60,
                desc: "分钟",
              },
            ],
            i = "",
            a = 0,
            s = n.length;
          a < s;
          a++
        ) {
          var r = e / n[a].time;
          if (
            !(a !== n.length - 1 && r > 0 && r <= 1) &&
            ((r = Math.ceil(r)), r > 0)
          ) {
            i = r + n[a].desc + "后";
            break;
          }
        }
        return "".concat(i, "过期");
      }
      return "";
    },
    getShareList() {
      this.shareList = [];
      this.axios.get("/api/sharefiles").then((response) => {
        if (response.data.errno === 0) {
          this.shareList = response.data.list;
        } else {
          this.ElNotification({
            title: "失败",
            message: response.data.show_msg,
            type: "error",
          });
        }
      });
    },
    reshare(shareId) {
      this.axios.get("/api/reshare/" + shareId).then((response) => {
        if (response.data.errno == 0) {
          this.ElNotification({
            title: "成功",
            message: "分享成功",
            type: "success",
          });
          setTimeout(() => {
            this.getShareList();
          }, 1000);
        } else {
          this.ElNotification({
            title: "失败",
            message: response.data.show_msg,
            type: "error",
          });
        }
      });
    },
    cancelShare(shareId) {
      this.axios.get("/api/cancelshare/" + shareId).then((response) => {
        if (response.data.errno == 0) {
          this.ElNotification({
            title: "成功",
            message: "取消分享成功",
            type: "success",
          });
          setTimeout(() => {
            this.getShareList();
          }, 1000);
        } else {
          this.ElNotification({
            title: "失败",
            message: response.data.show_msg,
            type: "error",
          });
        }
      });
    },
    copyLink(row) {
      let link = row.shortlink;
      this.axios.get("/api/getpwd/" + row.shareId).then((response) => {
        if (response.data.errno == 0) {
          if (response.data.pwd) {
            link += "?pwd=" + response.data.pwd;
          }
          this.ElNotification({
            title: "成功",
            message: "复制成功",
            type: "success",
          });
          this.clip.copy(link);
        }
      });
    }
  },
};
</script>

<style lang="scss">
.el-row {
  margin-bottom: 20px;
}
.el-link {
  margin-right: 8px;
}
.el-link .el-icon--right.el-icon {
  vertical-align: text-bottom;
}
</style>
