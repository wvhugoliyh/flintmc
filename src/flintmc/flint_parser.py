from lark import Transformer

from flintmc.nodes.definitions import (
  FuncDef,
  TickDef,
  LoadDef,
)

from flintmc.nodes.statements import (
  stmt,
  Assignment,
  FuncCall,
  Repeat,
)

from flintmc.nodes.expression import (
  MathBinaryOp,
  MathNeg,
  LogicBinaryOp,
  LogicNot,
  Comparison,
  EntityProp,
)

from flintmc.utils import filter_by_type

class FlintParser(Transformer):
  def start(self, children):
    return children

  def func_def(self, children):
    return FuncDef(
      children[0],
      filter_by_type(children[1::], str),
      filter_by_type(children[1::], stmt)
    )

  def tick_def(self, children):
    return TickDef(children[0], children[1::])

  def load_def(self, children):
    return LoadDef(children[0], children[1::])


  def assignment(self, children):
    return Assignment(children[0], children[1])

  def func_call(self, children):
    return FuncCall(children[0], children[1::])

  def conditional(self, children):
    return Conditional(
      children[0],
      filter_by_type(children[1::], Elif),
      children[-1] if isinstance(children[-1], Else) else None
    )

  def repeat(self, children):
    return Repeat(children[0], children[1::])

  
  def if_stmt(self, children):
    return If(children[0], children[1::])

  def elif_stmt(self, children):
    return Elif(children[0], children[1::])

  def else_stmt(self, children):
    return statements.Else(children[::])

  
  def expr(self, children):
    return MathBinaryOp(children[0], children[1], children[2])

  def term(self, children):
    return MathBinaryOp(children[0], children[1], children[2])

  def signed_power(self, children):
    return (
      children[-1]
      if children.count("-") % 2 == 0
      else MathNeg(children[-1])
    )

  def power(self, children):
    return MathBinaryOp(children[0], "^", children[1])

  def entity_prop(self, children):
    return EntityProp(children[0], children[1::])
  
  def disjunction(self, children):
    return LogicBinaryOp(children[0], "||", children[1])

  def conjunction(self, children):
    return LogicBinaryOp(children[0], "&&", children[1])

  def logic_not(self, children):
    return LogicNot(children[0])
  
  def comparison(self, children):
    return Comparison(children[0], children[1], children[2])


  def ID(self, token):
    return str(token)

  def ENTITY_SEL(self, token):
    return str(token)
    
  def INT(self, token):
    return int(token)

  def DOUBLE(self, token):
    return float(token)

  def BOOL(self, token):
    return bool(token)

  def SIGN(self, token):
    return str(token)

  def MUL_OP(self, token):
    return str(token)

  def COMPARATOR(self, token):
    return str(token)