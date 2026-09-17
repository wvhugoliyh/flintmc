from pathlib import Path
from typing import Any

from flintmc.nodes.definitions import (
  definitionT,
  FuncDef,
  TickDef,
  LoadDef,
)

from flintmc.nodes.statements import (
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

def sort_ast(ast: list, /, *, namespace: str = "minecraft") -> dict:
  """ Takes the AST and sorts the nodes into multiple files. """

  def sort_stmts(stmts: list[stmtT], /) -> dict:
    file_map: dict[Path, Any] = {}

    conditionals = filter_by_type(stmts, Conditional)
    executes = filter_by_type(stmts, Execute)
    repeats = filter_by_type(stmts, Repeat)

    for i, conditional in enumerate(conditionals):
      file_map[Path(f"if-{i}")] = conditional.if_stmt.stmts
    
      for j, elif_stmt in enumerate(conditional.elif_stmts):
        file_map[Path(f"elif-{i}-{j}")] = elif_stmt.stmts

      if conditional.else_stmt:
        file_map[Path(f"else-{i}")] = else_stmt.stmts

    for i, execute in enumerate(executes):
      file_map[Path(f"exec-{i}")] = execute.stmts

    for i, repeat in enumerate(repeats):
      file_map[Path(f"repeat-{i}")] = repeat.stmts
    return file_map

  def recursive_sort(
    flat_dir_tree: dict[Path, definitionT | stmtT],
    stmts: list[stmtT],
    /,
    id: str,
    *,
    path: Path
  ):

    flat_dir_tree[path / f"{id}.mcfunction"] = stmts

    for statement in stmts:
      for file_name, file_content in sort_stmts(stmts).items():
        flat_dir_tree.update({
          path / f"{id}-subfuncs" / file_name: file_content
        })

        recursive_sort(
          flat_dir_tree,
          file_content, 
          id=file_name,
          path=path / f"{id}-subfuncs"
        )

  flat_dir_tree = {}

  tick_defs = []
  load_defs = []

  for definition in ast:
    if isinstance(definition, TickDef):
      tick_defs.append(definition.id)

    if isinstance(definition, LoadDef):
      load_defs.append(definition.id)

    recursive_sort(
      flat_dir_tree,
      definition.stmts,
      id=definition.id,
      path=Path(f"data/{namespace}/function")
    )

  flat_dir_tree[Path("data/minecraft/tags/function/tick.json")] = '{"value":' + str(tick_defs) + '}'
  flat_dir_tree[Path("data/minecraft/tags/function/load.json")] = '{"value":' + str(load_defs) + '}'
  return flat_dir_tree