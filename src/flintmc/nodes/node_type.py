class NodeType:
  def __repr__(self) -> str:
    str_repr = f"{type(self).__name__}:"

    for attr, value in vars(self).items():
      str_repr = str_repr + f"\n  {attr}:\n    {value}"

    return str_repr