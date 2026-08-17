from lark import Transformer

from flintmc.nodes import (
  statements,
  definitions,
  conditional_parts,
  expression,
)

from flintmc.utils import filter_by_type

class FlintParser(Transformer):
  def start(self, children):
    return children

  def func_def(self, children):
    return definitions.FuncDef(
      children[0],
      filter_by_type(children[1::], str),
      filter_by_type(children[1::], statements.stmt)
    )

  def tick_def(self, children):
    return definitions.TickDef(children)

  def load_def(self, children):
    return definitions.LoadDef(children)


  def assignment(self, children):
    return statements.Assignment(children[0], children[1])

  def func_call(self, children):
    return statements.FuncCall(children[0], children[1::])

  def conditional(self, children):
    return statements.Conditional(
      children[0],
      filter_by_type(children[1::], conditional_parts.Elif),
      children[-1] if isinstance(children[-1], conditional_parts.Else) else None
    )

  def repeat(self, children):
    return statements.Repeat(children[0], children[1::])

  
  def if_stmt(self, children):
    return conditional_parts.If(children[0], children[1::])

  def elif_stmt(self, children):
    return conditional_parts.Elif(children[0], children[1::])

  def else_stmt(self, children):
    return conditional_parts.Else(children[::])

  
  def expr(self, children):
    return expression.MathBinaryOp(children[0], children[1], children[2])

  def term(self, children):
    return expression.MathBinaryOp(children[0], children[1], children[2])

  def signed_power(self, children):
    return (
      children[-1]
      if children.count("-") % 2 == 0
      else expression.MathNeg(children[-1])
    )

  def power(self, children):
    return expression.MathBinaryOp(children[0], "^", children[1])

  def disjunction(self, children):
    return expression.LogicBinaryOp(children[0], "||", children[1])

  def conjunction(self, children):
    return expression.LogicBinaryOp(children[0], "&&", children[1])

  def logic_not(self, children):
    return expression.LogicNot(children[0])
  
  def comparison(self, children):
    return expression.Comparison(children[0], children[1], children[2])


  def ID(self, token):
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