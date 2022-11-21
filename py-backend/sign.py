__all__ = ['sign']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['x', 'g', 'l', 'u', 'o', 'b', 'f', 'm', 'v', 'w', 'd', 's', 'y', 'h', 'p', 'a', 'c', 'A', 'C'])
@Js
def PyJsHoisted_o_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'e', 't', 'i'])
    var.put('n', ((Js(65535.0)&var.get('e'))+(Js(65535.0)&var.get('t'))))
    var.put('i', (((var.get('e')>>Js(16.0))+(var.get('t')>>Js(16.0)))+(var.get('n')>>Js(16.0))))
    return ((var.get('i')<<Js(16.0))|(Js(65535.0)&var.get('n')))
PyJsHoisted_o_.func_name = 'o'
var.put('o', PyJsHoisted_o_)
@Js
def PyJsHoisted_s_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 't'])
    return ((var.get('e')<<var.get('t'))|PyJsBshift(var.get('e'),(Js(32.0)-var.get('t'))))
PyJsHoisted_s_.func_name = 's'
var.put('s', PyJsHoisted_s_)
@Js
def PyJsHoisted_a_(e, t, n, i, r, a, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'i':i, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'a', 'e', 'r', 'n', 't'])
    return var.get('o')(var.get('s')(var.get('o')(var.get('o')(var.get('t'), var.get('e')), var.get('o')(var.get('i'), var.get('a'))), var.get('r')), var.get('n'))
PyJsHoisted_a_.func_name = 'a'
var.put('a', PyJsHoisted_a_)
@Js
def PyJsHoisted_c_(e, t, n, i, r, o, s, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'i':i, 'r':r, 'o':o, 's':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 's', 'e', 'r', 'o', 'n', 't'])
    return var.get('a')(((var.get('t')&var.get('n'))|((~var.get('t'))&var.get('i'))), var.get('e'), var.get('t'), var.get('r'), var.get('o'), var.get('s'))
PyJsHoisted_c_.func_name = 'c'
var.put('c', PyJsHoisted_c_)
@Js
def PyJsHoisted_l_(e, t, n, i, r, o, s, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'i':i, 'r':r, 'o':o, 's':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 's', 'e', 'r', 'o', 'n', 't'])
    return var.get('a')(((var.get('t')&var.get('i'))|(var.get('n')&(~var.get('i')))), var.get('e'), var.get('t'), var.get('r'), var.get('o'), var.get('s'))
PyJsHoisted_l_.func_name = 'l'
var.put('l', PyJsHoisted_l_)
@Js
def PyJsHoisted_u_(e, t, n, i, r, o, s, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'i':i, 'r':r, 'o':o, 's':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 's', 'e', 'r', 'o', 'n', 't'])
    return var.get('a')(((var.get('t')^var.get('n'))^var.get('i')), var.get('e'), var.get('t'), var.get('r'), var.get('o'), var.get('s'))
PyJsHoisted_u_.func_name = 'u'
var.put('u', PyJsHoisted_u_)
@Js
def PyJsHoisted_d_(e, t, n, i, r, o, s, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'i':i, 'r':r, 'o':o, 's':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 's', 'e', 'r', 'o', 'n', 't'])
    return var.get('a')((var.get('n')^(var.get('t')|(~var.get('i')))), var.get('e'), var.get('t'), var.get('r'), var.get('o'), var.get('s'))
PyJsHoisted_d_.func_name = 'd'
var.put('d', PyJsHoisted_d_)
@Js
def PyJsHoisted_A_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 's', 'A', 'f', 'h', 'p', 'a', 'e', 'r', 'n', 't'])
    pass
    PyJsComma(var.get('e').put((var.get('t')>>Js(5.0)), (Js(128.0)<<(var.get('t')%Js(32.0))), '|'),var.get('e').put((Js(14.0)+(PyJsBshift((var.get('t')+Js(64.0)),Js(9.0))<<Js(4.0))), var.get('t')))
    var.put('A', Js(1732584193.0))
    var.put('f', (-Js(271733879.0)))
    var.put('p', (-Js(1732584194.0)))
    var.put('h', Js(271733878.0))
    #for JS loop
    var.put('n', Js(0.0))
    while (var.get('n')<var.get('e').get('length')):
        def PyJs_LONG_0_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', var.get('A')),var.put('r', var.get('f'))),var.put('s', var.get('p'))),var.put('a', var.get('h'))),var.put('A', var.get('c')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get(var.get('n')), Js(7.0), (-Js(680876936.0))))),var.put('h', var.get('c')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(1.0))), Js(12.0), (-Js(389564586.0))))),var.put('p', var.get('c')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(2.0))), Js(17.0), Js(606105819.0)))),var.put('f', var.get('c')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))),var.put('A', var.get('c')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(4.0))), Js(7.0), (-Js(176418897.0))))),var.put('h', var.get('c')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(5.0))), Js(12.0), Js(1200080426.0)))),var.put('p', var.get('c')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))),var.put('f', var.get('c')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(7.0))), Js(22.0), (-Js(45705983.0))))),var.put('A', var.get('c')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(8.0))), Js(7.0), Js(1770035416.0)))),var.put('h', var.get('c')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))),var.put('p', var.get('c')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(10.0))), Js(17.0), (-Js(42063.0))))),var.put('f', var.get('c')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))),var.put('A', var.get('c')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(12.0))), Js(7.0), Js(1804603682.0)))),var.put('h', var.get('c')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(13.0))), Js(12.0), (-Js(40341101.0))))),var.put('p', var.get('c')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))),var.put('f', var.get('c')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(15.0))), Js(22.0), Js(1236535329.0)))),var.put('A', var.get('l')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(1.0))), Js(5.0), (-Js(165796510.0))))),var.put('h', var.get('l')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))),var.put('p', var.get('l')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(11.0))), Js(14.0), Js(643717713.0)))),var.put('f', var.get('l')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get(var.get('n')), Js(20.0), (-Js(373897302.0))))),var.put('A', var.get('l')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(5.0))), Js(5.0), (-Js(701558691.0))))),var.put('h', var.get('l')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(10.0))), Js(9.0), Js(38016083.0)))),var.put('p', var.get('l')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(15.0))), Js(14.0), (-Js(660478335.0))))),var.put('f', var.get('l')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(4.0))), Js(20.0), (-Js(405537848.0))))),var.put('A', var.get('l')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(9.0))), Js(5.0), Js(568446438.0)))),var.put('h', var.get('l')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))),var.put('p', var.get('l')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(3.0))), Js(14.0), (-Js(187363961.0))))),var.put('f', var.get('l')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(8.0))), Js(20.0), Js(1163531501.0)))),var.put('A', var.get('l')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))),var.put('h', var.get('l')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(2.0))), Js(9.0), (-Js(51403784.0))))),var.put('p', var.get('l')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(7.0))), Js(14.0), Js(1735328473.0)))),var.put('f', var.get('l')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))),var.put('A', var.get('u')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(5.0))), Js(4.0), (-Js(378558.0))))),var.put('h', var.get('u')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))),var.put('p', var.get('u')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(11.0))), Js(16.0), Js(1839030562.0)))),var.put('f', var.get('u')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(14.0))), Js(23.0), (-Js(35309556.0))))),var.put('A', var.get('u')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))),var.put('h', var.get('u')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(4.0))), Js(11.0), Js(1272893353.0)))),var.put('p', var.get('u')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(7.0))), Js(16.0), (-Js(155497632.0))))),var.put('f', var.get('u')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))),var.put('A', var.get('u')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(13.0))), Js(4.0), Js(681279174.0)))),var.put('h', var.get('u')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get(var.get('n')), Js(11.0), (-Js(358537222.0))))),var.put('p', var.get('u')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(3.0))), Js(16.0), (-Js(722521979.0))))),var.put('f', var.get('u')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(6.0))), Js(23.0), Js(76029189.0)))),var.put('A', var.get('u')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(9.0))), Js(4.0), (-Js(640364487.0))))),var.put('h', var.get('u')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(12.0))), Js(11.0), (-Js(421815835.0))))),var.put('p', var.get('u')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(15.0))), Js(16.0), Js(530742520.0)))),var.put('f', var.get('u')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(2.0))), Js(23.0), (-Js(995338651.0))))),var.put('A', var.get('d')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get(var.get('n')), Js(6.0), (-Js(198630844.0))))),var.put('h', var.get('d')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(7.0))), Js(10.0), Js(1126891415.0)))),var.put('p', var.get('d')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))),var.put('f', var.get('d')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(5.0))), Js(21.0), (-Js(57434055.0))))),var.put('A', var.get('d')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(12.0))), Js(6.0), Js(1700485571.0)))),var.put('h', var.get('d')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))),var.put('p', var.get('d')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(10.0))), Js(15.0), (-Js(1051523.0))))),var.put('f', var.get('d')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))),var.put('A', var.get('d')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(8.0))), Js(6.0), Js(1873313359.0)))),var.put('h', var.get('d')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(15.0))), Js(10.0), (-Js(30611744.0))))),var.put('p', var.get('d')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))),var.put('f', var.get('d')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(13.0))), Js(21.0), Js(1309151649.0)))),var.put('A', var.get('d')(var.get('A'), var.get('f'), var.get('p'), var.get('h'), var.get('e').get((var.get('n')+Js(4.0))), Js(6.0), (-Js(145523070.0))))),var.put('h', var.get('d')(var.get('h'), var.get('A'), var.get('f'), var.get('p'), var.get('e').get((var.get('n')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))),var.put('p', var.get('d')(var.get('p'), var.get('h'), var.get('A'), var.get('f'), var.get('e').get((var.get('n')+Js(2.0))), Js(15.0), Js(718787259.0)))),var.put('f', var.get('d')(var.get('f'), var.get('p'), var.get('h'), var.get('A'), var.get('e').get((var.get('n')+Js(9.0))), Js(21.0), (-Js(343485551.0))))),var.put('A', var.get('o')(var.get('A'), var.get('i')))),var.put('f', var.get('o')(var.get('f'), var.get('r')))),var.put('p', var.get('o')(var.get('p'), var.get('s')))),var.put('h', var.get('o')(var.get('h'), var.get('a'))))
        PyJs_LONG_0_()
        # update
        var.put('n', Js(16.0), '+')
    return Js([var.get('A'), var.get('f'), var.get('p'), var.get('h')])
PyJsHoisted_A_.func_name = 'A'
var.put('A', PyJsHoisted_A_)
@Js
def PyJsHoisted_f_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'e', 't', 'i'])
    var.put('n', Js(''))
    var.put('i', (Js(32.0)*var.get('e').get('length')))
    #for JS loop
    var.put('t', Js(0.0))
    while (var.get('t')<var.get('i')):
        var.put('n', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('e').get((var.get('t')>>Js(5.0))),(var.get('t')%Js(32.0)))&Js(255.0))), '+')
        # update
        var.put('t', Js(8.0), '+')
    return var.get('n')
PyJsHoisted_f_.func_name = 'f'
var.put('f', PyJsHoisted_f_)
@Js
def PyJsHoisted_p_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'e', 't', 'i'])
    var.put('n', Js([]))
    #for JS loop
    PyJsComma(var.get('n').put(((var.get('e').get('length')>>Js(2.0))-Js(1.0)), PyJsComma(Js(0.0), Js(None))),var.put('t', Js(0.0)))
    while (var.get('t')<var.get('n').get('length')):
        var.get('n').put(var.get('t'), Js(0.0))
        # update
        var.put('t', Js(1.0), '+')
    var.put('i', (Js(8.0)*var.get('e').get('length')))
    #for JS loop
    var.put('t', Js(0.0))
    while (var.get('t')<var.get('i')):
        var.get('n').put((var.get('t')>>Js(5.0)), ((Js(255.0)&var.get('e').callprop('charCodeAt', (var.get('t')/Js(8.0))))<<(var.get('t')%Js(32.0))), '|')
        # update
        var.put('t', Js(8.0), '+')
    return var.get('n')
PyJsHoisted_p_.func_name = 'p'
var.put('p', PyJsHoisted_p_)
@Js
def PyJsHoisted_h_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('f')(var.get('A')(var.get('p')(var.get('e')), (Js(8.0)*var.get('e').get('length'))))
PyJsHoisted_h_.func_name = 'h'
var.put('h', PyJsHoisted_h_)
@Js
def PyJsHoisted_m_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 's', 'e', 'r', 'o', 'n', 't'])
    var.put('r', var.get('p')(var.get('e')))
    var.put('o', Js([]))
    var.put('s', Js([]))
    #for JS loop
    PyJsComma(PyJsComma(var.get('o').put('15', var.get('s').put('15', PyJsComma(Js(0.0), Js(None)))),((var.get('r').get('length')>Js(16.0)) and var.put('r', var.get('A')(var.get('r'), (Js(8.0)*var.get('e').get('length')))))),var.put('n', Js(0.0)))
    while (var.get('n')<Js(16.0)):
        PyJsComma(var.get('o').put(var.get('n'), (Js(909522486.0)^var.get('r').get(var.get('n')))),var.get('s').put(var.get('n'), (Js(1549556828.0)^var.get('r').get(var.get('n')))))
        # update
        var.put('n', Js(1.0), '+')
    return PyJsComma(var.put('i', var.get('A')(var.get('o').callprop('concat', var.get('p')(var.get('t'))), (Js(512.0)+(Js(8.0)*var.get('t').get('length'))))),var.get('f')(var.get('A')(var.get('s').callprop('concat', var.get('i')), Js(640.0))))
PyJsHoisted_m_.func_name = 'm'
var.put('m', PyJsHoisted_m_)
@Js
def PyJsHoisted_v_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'e', 'r', 'n', 't'])
    var.put('i', Js('0123456789abcdef'))
    var.put('r', Js(''))
    #for JS loop
    var.put('n', Js(0.0))
    while (var.get('n')<var.get('e').get('length')):
        PyJsComma(var.put('t', var.get('e').callprop('charCodeAt', var.get('n'))),var.put('r', (var.get('i').callprop('charAt', (PyJsBshift(var.get('t'),Js(4.0))&Js(15.0)))+var.get('i').callprop('charAt', (Js(15.0)&var.get('t')))), '+'))
        # update
        var.put('n', Js(1.0), '+')
    return var.get('r')
PyJsHoisted_v_.func_name = 'v'
var.put('v', PyJsHoisted_v_)
@Js
def PyJsHoisted_g_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('unescape')(var.get('encodeURIComponent')(var.get('e')))
PyJsHoisted_g_.func_name = 'g'
var.put('g', PyJsHoisted_g_)
@Js
def PyJsHoisted_y_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('h')(var.get('g')(var.get('e')))
PyJsHoisted_y_.func_name = 'y'
var.put('y', PyJsHoisted_y_)
@Js
def PyJsHoisted_b_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('v')(var.get('y')(var.get('e')))
PyJsHoisted_b_.func_name = 'b'
var.put('b', PyJsHoisted_b_)
@Js
def PyJsHoisted_w_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 't'])
    return var.get('m')(var.get('g')(var.get('e')), var.get('g')(var.get('t')))
PyJsHoisted_w_.func_name = 'w'
var.put('w', PyJsHoisted_w_)
@Js
def PyJsHoisted_C_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 't'])
    return var.get('v')(var.get('w')(var.get('e'), var.get('t')))
PyJsHoisted_C_.func_name = 'C'
var.put('C', PyJsHoisted_C_)
@Js
def PyJsHoisted_x_(e, t, n, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'e', 't'])
    return ((var.get('w')(var.get('t'), var.get('e')) if var.get('n') else var.get('C')(var.get('t'), var.get('e'))) if var.get('t') else (var.get('y')(var.get('e')) if var.get('n') else var.get('b')(var.get('e'))))
PyJsHoisted_x_.func_name = 'x'
var.put('x', PyJsHoisted_x_)
Js('use strict')
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
sign = var.to_python()