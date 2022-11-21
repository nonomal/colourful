"use strict";
function o(e, t) {
    var n = (65535 & e) + (65535 & t)
    , i = (e >> 16) + (t >> 16) + (n >> 16);
    return i << 16 | 65535 & n
}
function s(e, t) {
    return e << t | e >>> 32 - t
}
function a(e, t, n, i, r, a) {
    return o(s(o(o(t, e), o(i, a)), r), n)
}
function c(e, t, n, i, r, o, s) {
    return a(t & n | ~t & i, e, t, r, o, s)
}
function l(e, t, n, i, r, o, s) {
    return a(t & i | n & ~i, e, t, r, o, s)
}
function u(e, t, n, i, r, o, s) {
    return a(t ^ n ^ i, e, t, r, o, s)
}
function d(e, t, n, i, r, o, s) {
    return a(n ^ (t | ~i), e, t, r, o, s)
}
function A(e, t) {
    var n, i, r, s, a;
    e[t >> 5] |= 128 << t % 32,
    e[14 + (t + 64 >>> 9 << 4)] = t;
    var A = 1732584193
    , f = -271733879
    , p = -1732584194
    , h = 271733878;
    for (n = 0; n < e.length; n += 16)
        i = A,
        r = f,
        s = p,
        a = h,
        A = c(A, f, p, h, e[n], 7, -680876936),
        h = c(h, A, f, p, e[n + 1], 12, -389564586),
        p = c(p, h, A, f, e[n + 2], 17, 606105819),
        f = c(f, p, h, A, e[n + 3], 22, -1044525330),
        A = c(A, f, p, h, e[n + 4], 7, -176418897),
        h = c(h, A, f, p, e[n + 5], 12, 1200080426),
        p = c(p, h, A, f, e[n + 6], 17, -1473231341),
        f = c(f, p, h, A, e[n + 7], 22, -45705983),
        A = c(A, f, p, h, e[n + 8], 7, 1770035416),
        h = c(h, A, f, p, e[n + 9], 12, -1958414417),
        p = c(p, h, A, f, e[n + 10], 17, -42063),
        f = c(f, p, h, A, e[n + 11], 22, -1990404162),
        A = c(A, f, p, h, e[n + 12], 7, 1804603682),
        h = c(h, A, f, p, e[n + 13], 12, -40341101),
        p = c(p, h, A, f, e[n + 14], 17, -1502002290),
        f = c(f, p, h, A, e[n + 15], 22, 1236535329),
        A = l(A, f, p, h, e[n + 1], 5, -165796510),
        h = l(h, A, f, p, e[n + 6], 9, -1069501632),
        p = l(p, h, A, f, e[n + 11], 14, 643717713),
        f = l(f, p, h, A, e[n], 20, -373897302),
        A = l(A, f, p, h, e[n + 5], 5, -701558691),
        h = l(h, A, f, p, e[n + 10], 9, 38016083),
        p = l(p, h, A, f, e[n + 15], 14, -660478335),
        f = l(f, p, h, A, e[n + 4], 20, -405537848),
        A = l(A, f, p, h, e[n + 9], 5, 568446438),
        h = l(h, A, f, p, e[n + 14], 9, -1019803690),
        p = l(p, h, A, f, e[n + 3], 14, -187363961),
        f = l(f, p, h, A, e[n + 8], 20, 1163531501),
        A = l(A, f, p, h, e[n + 13], 5, -1444681467),
        h = l(h, A, f, p, e[n + 2], 9, -51403784),
        p = l(p, h, A, f, e[n + 7], 14, 1735328473),
        f = l(f, p, h, A, e[n + 12], 20, -1926607734),
        A = u(A, f, p, h, e[n + 5], 4, -378558),
        h = u(h, A, f, p, e[n + 8], 11, -2022574463),
        p = u(p, h, A, f, e[n + 11], 16, 1839030562),
        f = u(f, p, h, A, e[n + 14], 23, -35309556),
        A = u(A, f, p, h, e[n + 1], 4, -1530992060),
        h = u(h, A, f, p, e[n + 4], 11, 1272893353),
        p = u(p, h, A, f, e[n + 7], 16, -155497632),
        f = u(f, p, h, A, e[n + 10], 23, -1094730640),
        A = u(A, f, p, h, e[n + 13], 4, 681279174),
        h = u(h, A, f, p, e[n], 11, -358537222),
        p = u(p, h, A, f, e[n + 3], 16, -722521979),
        f = u(f, p, h, A, e[n + 6], 23, 76029189),
        A = u(A, f, p, h, e[n + 9], 4, -640364487),
        h = u(h, A, f, p, e[n + 12], 11, -421815835),
        p = u(p, h, A, f, e[n + 15], 16, 530742520),
        f = u(f, p, h, A, e[n + 2], 23, -995338651),
        A = d(A, f, p, h, e[n], 6, -198630844),
        h = d(h, A, f, p, e[n + 7], 10, 1126891415),
        p = d(p, h, A, f, e[n + 14], 15, -1416354905),
        f = d(f, p, h, A, e[n + 5], 21, -57434055),
        A = d(A, f, p, h, e[n + 12], 6, 1700485571),
        h = d(h, A, f, p, e[n + 3], 10, -1894986606),
        p = d(p, h, A, f, e[n + 10], 15, -1051523),
        f = d(f, p, h, A, e[n + 1], 21, -2054922799),
        A = d(A, f, p, h, e[n + 8], 6, 1873313359),
        h = d(h, A, f, p, e[n + 15], 10, -30611744),
        p = d(p, h, A, f, e[n + 6], 15, -1560198380),
        f = d(f, p, h, A, e[n + 13], 21, 1309151649),
        A = d(A, f, p, h, e[n + 4], 6, -145523070),
        h = d(h, A, f, p, e[n + 11], 10, -1120210379),
        p = d(p, h, A, f, e[n + 2], 15, 718787259),
        f = d(f, p, h, A, e[n + 9], 21, -343485551),
        A = o(A, i),
        f = o(f, r),
        p = o(p, s),
        h = o(h, a);
    return [A, f, p, h]
}
function f(e) {
    var t, n = "", i = 32 * e.length;
    for (t = 0; t < i; t += 8)
        n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
    return n
}
function p(e) {
    var t, n = [];
    for (n[(e.length >> 2) - 1] = void 0,
    t = 0; t < n.length; t += 1)
        n[t] = 0;
    var i = 8 * e.length;
    for (t = 0; t < i; t += 8)
        n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return n
}
function h(e) {
    return f(A(p(e), 8 * e.length))
}
function m(e, t) {
    var n, i, r = p(e), o = [], s = [];
    for (o[15] = s[15] = void 0,
    r.length > 16 && (r = A(r, 8 * e.length)),
    n = 0; n < 16; n += 1)
        o[n] = 909522486 ^ r[n],
        s[n] = 1549556828 ^ r[n];
    return i = A(o.concat(p(t)), 512 + 8 * t.length),
    f(A(s.concat(i), 640))
}
function v(e) {
    var t, n, i = "0123456789abcdef", r = "";
    for (n = 0; n < e.length; n += 1)
        t = e.charCodeAt(n),
        r += i.charAt(t >>> 4 & 15) + i.charAt(15 & t);
    return r
}
function g(e) {
    return unescape(encodeURIComponent(e))
}
function y(e) {
    return h(g(e))
}
function b(e) {
    return v(y(e))
}
function w(e, t) {
    return m(g(e), g(t))
}
function C(e, t) {
    return v(w(e, t))
}
function x(e, t, n) {
    return t ? n ? w(t, e) : C(t, e) : n ? y(e) : b(e)
}