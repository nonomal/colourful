<template>
  <div class="common-layout">
    <h3>文件列表</h3>
    <el-button
      type="primary"
      :link="true"
      @click="() => {
        if (dir.length > 1) {
          dir.pop();
        }
        getFileList();
      }"
      >返回上一级</el-button
    >
    <el-row>
      <el-col>
        <el-table
          stripe
          :data="shareList.slice((page - 1) * pageSize, page * pageSize)"
        >
          <el-table-column label="fs_id" prop="fs_id" width="200px">
          </el-table-column>
          <el-table-column label="文件名" prop="server_filename" width="500px"/>
          <el-table-column label="路径" prop="path" >
            <template v-slot="scope">
              <el-button
                v-if="scope.row.isdir === 1"
                type="primary"
                :link="true"
                @click="() => {
                  dir.push(scope.row.path);
                  getFileList();
                }"
                >{{ scope.row.path }}</el-button
              >
            </template>
          </el-table-column>
          <el-table-column label="操作" width="50px">
            <template v-slot="scope">
              <el-button
                type="primary"
                size="small"
                @click="share(scope.row.fs_id)"
                >分享</el-button
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
      dir: ["/"]
    };
  },

  mounted() {
    this.getFileList();
  },
  methods: {
    handleSizeChange(val) {
      this.page = 1;
      this.pageSize = val;
    },
    handleCurrentChange(val) {
      this.page = val;
    },
    getFileList() {
      this.shareList = [];
      this.axios.get("/api/files?dir=" + this.dir[this.dir.length - 1] + "&page=1&num=10000").then((response) => {
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
    share(fsId) {
      this.axios.get("/api/getfileshare/" + fsId).then((response) => {
        if (response.data.errno == 0) {
          this.ElNotification({
            title: "分享成功",
            message: response.data.url,
            type: "success",
          });
        } else {
          this.ElNotification({
            title: "失败",
            message: response.data.show_msg,
            type: "error",
          });
        }
      });
    }
  },
};
</script>