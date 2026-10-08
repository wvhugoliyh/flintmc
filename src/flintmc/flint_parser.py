from lark import Transformer

from flintmc.nodes import (
  FuncDef,
  TickDef,
  LoadDef,
  stmtT,
  Assignment,
  FuncCall,
  Conditional,
  Repeat,
  Execute,
  Run,
  If,
  Elif,
  Else,
  MathBinaryOp,
  MathNeg,
  LogicBinaryOp,
  LogicNot,
  Comparison,
  EntityProp,
  ResourceLocation,
  Variable,
) 

class FlintParser(Transformer):
  """The parser used to generate an AST from flint code."""

  def start(self, children: list) -> list:
    return children

  def namespace_metadef(self, children: list) -> None:
    self.namespace = children[0]

  def func_def(self, children: list) -> FuncDef:
    return FuncDef(
      children[0],
      [child for child in children[::] if isinstance(child, str)],
      [child for child in children[::] if isinstance(child, stmtT.__value__)]
    )

  def tick_def(self, children: list) -> TickDef:
    return TickDef(children[0], children[1::])

  def load_def(self, children: list) -> LoadDef:
    return LoadDef(children[0], children[1::])


  def assignment(self, children: list) -> Assignment:
    return Assignment(
      children[0],
      children[1]
    )

  def func_call(self, children: list) -> FuncCall:
    return FuncCall(children[0], children[1::])

  def conditional(self, children: list) -> Conditional:
    return Conditional(
      children[0],
      [child for child in children[1::] if isinstance(child, Elif)],
      children[-1] if isinstance(children[-1], Else) else None
    )

  def repeat(self, children: list) -> Repeat:
    return Repeat(children[0], children[1::])

  def execute(self, children: list) -> Execute:
    return Execute(children[0], children[1::])

  def run(self, children: list) -> Run:
    return Run(children[0])
  
  
  def if_stmt(self, children: list) -> If:
    return If(children[0], children[1::])

  def elif_stmt(self, children: list) -> Elif:
    return Elif(children[0], children[1::])

  def else_stmt(self, children: list) -> Else:
    return Else(children[::])

  
  def expr(self, children: list) -> MathBinaryOp:
    return MathBinaryOp(children[0], children[1], children[2])

  def term(self, children: list) -> MathBinaryOp:
    return MathBinaryOp(children[0], children[1], children[2])

  def signed_power(self, children: list) -> MathBinaryOp | MathNeg:
    return (
      children[-1] if children.count("-") % 2 == 0
      else MathNeg(children[-1])
    )

  def power(self, children: list) -> MathBinaryOp:
    return MathBinaryOp(children[0], "^", children[1])

  def entity_prop(self, children: list) -> EntityProp:
    return EntityProp(children[0], children[1::])

  def variable(self, children: list) -> Variable:
    return Variable(
      children[0] if len(children) == 2 
      else ResourceLocation(self.namespace, "vars"),
      children[-1]
    )
  
  def disjunction(self, children: list) -> LogicBinaryOp:
    return LogicBinaryOp(children[0], "||", children[1])

  def conjunction(self, children: list) -> LogicBinaryOp:
    return LogicBinaryOp(children[0], "&&", children[1])

  def logic_not(self, children: list) -> LogicNot:
    return LogicNot(children[0])
  
  def comparison(self, children: list) -> Comparison:
    return Comparison(children[0], children[1], children[2])


  def resource_loc(self, children: list) -> ResourceLocation:
    return ResourceLocation(children[0] if len(children) == 2
                            else getattr(self, "namespace", "minecraft"),
                            children[-1])

  def variable(self, children: list) -> Variable:
    return Variable(
      children[0] if len(children) == 2
      else ResourceLocation(self.namespace, "vars"),
      children[-1]
    )


  def USERNAME(self, token: Token) -> str:
    return str(token)

  def UUID(self, token: Token) -> str:
    return str(token)

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