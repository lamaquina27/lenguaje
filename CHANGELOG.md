# Cambioa en esta versión:
---

## Gramatica:
- programa: importaciones? instrucciones? PRINCIPAL LLAVE_IZQ instrucciones? LLAVE_DER;
---

## Visitor
- def visitPalabras(self, ctx):

- agregar funciones:

```
def visitVerdad(self,ctx):
        izq = self.visit(ctx.expresion_verdad(0))
        der = self.visit(ctx.expresion_verdad(1))
        
        if ctx.op.type == gramaticaParser.AND:
            return izq and der
        elif ctx.op.type == gramaticaParser.OR:
            return izq or der
    def visitParver(self,ctx):
        return self.visit(ctx.expresion_verdad()) 
```
---

## ¿Para qué?
- acepta \ como escape.

