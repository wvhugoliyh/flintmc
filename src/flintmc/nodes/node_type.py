from typewrap import dedent

class NodeType:
  def __repr__(self) -> str:
    str_repr = f"{type(self).__name__}:"

    for attr, value in vars(self):
      str_repr.append(dedent(f"  {attr}:\n    {value}"))

    return str_repr