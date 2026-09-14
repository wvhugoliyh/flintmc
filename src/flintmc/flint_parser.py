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
  Execute,
  Run,
  If,
  Elif,
  Else,
  ExecArg,
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
  """ The parser used to generate an AST from flint code. """

  def start(self, children: list) -> list[stmt]:
    return children

  def func_def(self, children: list) -> FuncDef:
    return FuncDef(
      children[0],
      filter_by_type(children[1::], str),
      filter_by_type(children[1::], stmt.__value__)
    )

  def tick_def(self, children: list) -> TickDef:
    return TickDef(children[0], children[1::])

  def load_def(self, children: list) -> LoadDef:
    return LoadDef(children[0], children[1::])


  def assignment(self, children: list) -> Assignment:
    return Assignment(children[0], children[1])

  def func_call(self, children: list) -> FuncCall:
    return FuncCall(children[0], children[1::])

  def conditional(self, children: list) -> Conditional:
    return Conditional(
      children[0],
      filter_by_type(children[1::], Elif),
      children[-1] if isinstance(children[-1], Else) else None
    )

  def repeat(self, children: list) -> Repeat:
    return Repeat(children[0], children[1::])

  def execute(self, children: list) -> Execute:
    return Execute(
      filter_by_type(children[::], ExecArg),
      filter_by_type(children[::], stmt.__value__)
    )

  def run(self, children: list) -> Run:
    return Run(children[0])
  
  
  def if_stmt(self, children: list) -> If:
    return If(children[0], children[1::])

  def elif_stmt(self, children: list) -> Elif:
    return Elif(children[0], children[1::])

  def else_stmt(self, children: list) -> Else:
    return Else(children[::])


  def exec_align(self, children: list) -> ExecArg:
    return ExecArg("align", children)

  def exec_anchored(self, children: list) -> ExecArg:
    return ExecArg("anchored", children)

  def exec_as(self, children: list) -> ExecArg:
    return ExecArg("as", children)

  def exec_at(self, children: list) -> ExecArg:
    return ExecArg("at", children)

  def exec_facing(self, children: list) -> ExecArg:
    return ExecArg("facing", children)

  def exec_facing_entity(self, children: list) -> ExecArg:
    return ExecArg("facing_entity", children)

  def exec_in(self, children: list) -> ExecArg:
    return ExecArg("in", children)

  def exec_on(self, children: list) -> ExecArg:
    return ExecArg("on", children)

  def exec_pos(self, children: list) -> ExecArg:
    return ExecArg("pos", children)

  def exec_pos_as(self, children: list) -> ExecArg:
    return ExecArg("pos_as", children)

  def exec_pos_over(self, children: list) -> ExecArg:
    return ExecArg("pos_over", children)

  def exec_rotated(self, children: list) -> ExecArg:
    return ExecArg("rotated", children)

  def exec_rotated_as(self, children: list) -> ExecArg:
    return ExecArg("rotated_as", children)

  def exec_summon(self, children: list) -> ExecArg:
    return ExecArg("summon", children)

  
  def expr(self, children: list) -> MathBinaryOp:
    return MathBinaryOp(children[0], children[1], children[2])

  def term(self, children: list) -> MathBinaryOp:
    return MathBinaryOp(children[0], children[1], children[2])

  def signed_power(self, children: list) -> MathBinaryOp | MathNeg:
    return (
      children[-1]
      if children.count("-") % 2 == 0
      else MathNeg(children[-1])
    )

  def power(self, children: list) -> MathBinaryOp:
    return MathBinaryOp(children[0], "^", children[1])

  def entity_prop(self, children: list) -> EntityProp:
    return EntityProp(children[0], children[1::])
  
  def disjunction(self, children: list) -> LogicBinaryOp:
    return LogicBinaryOp(children[0], "||", children[1])

  def conjunction(self, children: list) -> LogicBinaryOp:
    return LogicBinaryOp(children[0], "&&", children[1])

  def logic_not(self, children: list) -> LogicNot:
    return LogicNot(children[0])
  
  def comparison(self, children: list) -> Comparison:
    return Comparison(children[0], children[1], children[2])


  def ID(self, token: Token) -> str:
    return str(token)

  def ENTITY_SEL(self, token: Token) -> str:
    return str(token)
    
  def RAW(self, token: Token) -> str:
    return str(token)
    
  def INT(self, token: Token) -> int:
    return int(token)

  def DOUBLE(self, token: Token) -> float:
    return float(token)

  def BOOL(self, token: Token) -> bool:
    return bool(token)

  def SIGN(self, token: Token) -> str:
    return str(token)

  def MUL_OP(self, token: Token) -> str:
    return str(token)

  def COMPARATOR(self, token: Token) -> str:
    return str(token)