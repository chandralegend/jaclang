"""Abstract class for IR Passes for Jac."""
import pprint


class AstNode:
    """Abstract syntax tree node for Jac."""

    def __init__(self: "AstNode", parent: "AstNode", kid: list, line: int) -> None:
        """Initialize ast."""
        self.parent = parent
        self.kid = kid if kid else []
        self.line = line

    def __str__(self: "AstNode") -> str:
        """Return string representation of node."""
        return f"{str(type(self).__name__)}->[{self.line},{len(self.kid)} kids]"

    def __repr__(self: "AstNode") -> str:
        """Return string representation of node."""
        return str(self)

    def to_dict(self: "AstNode") -> dict:
        """Return dict representation of node."""
        return {
            "node": str(type(self).__name__),
            "kid": [x.to_dict() for x in self.kid],
            "line": self.line,
        }

    def print(self: "AstNode", depth: int = None) -> None:
        """Print ast."""
        pprint.PrettyPrinter(depth=depth).pprint(self.to_dict())


class Blank(AstNode):
    """Blank node type for Jac Ast."""

    def __init__(self: "Blank") -> None:
        """Initialize blank."""
        super().__init__(parent=None, kid=[], line=0)


class Token(AstNode):
    """Token node type for Jac Ast."""

    def __init__(
        self: "Token", name: str, value: str, *args: list, **kwargs: dict
    ) -> None:
        """Initialize token."""
        self.name = name
        self.value = value
        super().__init__(*args, **kwargs)


class Parse(AstNode):
    """Parse node type for Jac Ast."""

    def __init__(self: "Parse", name: str, *args: list, **kwargs: dict) -> None:
        """Initialize parse."""
        self.name = name
        super().__init__(*args, **kwargs)


class WholeBuild(AstNode):
    """Whole Program node type for Jac Ast."""

    def __init__(
        self: "WholeBuild", elements: list, *args: list, **kwargs: dict
    ) -> None:
        """Initialize whole program node."""
        self.elements = elements
        super().__init__(*args, **kwargs)


class DocString(AstNode):
    """DocString node type for Jac Ast."""

    def __init__(
        self: "DocString", value: AstNode, *args: list, **kwargs: dict
    ) -> None:
        """Initialize docstring node."""
        self.value = value
        super().__init__(*args, **kwargs)


class GlobalVars(AstNode):
    """GlobalVars node type for Jac Ast."""

    def __init__(
        self: "GlobalVars", access: AstNode, values: list, *args: list, **kwargs: dict
    ) -> None:
        """Initialize global var node."""
        self.access = access
        self.values = values
        super().__init__(*args, **kwargs)


class NamedAssign(AstNode):
    """NamedAssign node type for Jac Ast."""

    def __init__(
        self: "NamedAssign", name: AstNode, value: AstNode, *args: list, **kwargs: dict
    ) -> None:
        """Initialize named assign node."""
        self.name = name
        self.value = value
        super().__init__(*args, **kwargs)


class Test(AstNode):
    """Test node type for Jac Ast."""

    def __init__(
        self: "Test",
        name: AstNode,
        description: AstNode,
        body: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize test node."""
        self.name = name
        self.description = description
        self.body = body
        super().__init__(*args, **kwargs)


class Import(AstNode):
    """Import node type for Jac Ast."""

    def __init__(
        self: "Import",
        lang: AstNode,
        path: AstNode,
        alias: AstNode,
        items: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize import node."""
        self.lang = lang
        self.path = path
        self.alias = alias
        self.items = items
        super().__init__(*args, **kwargs)


class ModulePath(AstNode):
    """ModulePath node type for Jac Ast."""

    def __init__(self: "ModulePath", path: list, *args: list, **kwargs: dict) -> None:
        """Initialize module path node."""
        self.path = path
        super().__init__(*args, **kwargs)


class ModuleItem(AstNode):
    """ModuleItem node type for Jac Ast."""

    def __init__(
        self: "ModuleItem", name: AstNode, alias: AstNode, *args: list, **kwargs: dict
    ) -> None:
        """Initialize module item node."""
        self.name = name
        self.alias = alias
        super().__init__(*args, **kwargs)


class ObjectArch(AstNode):
    """ObjectArch node type for Jac Ast."""

    def __init__(
        self: "ObjectArch",
        name: AstNode,
        access: AstNode,
        base_classes: AstNode,
        body: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize object arch node."""
        self.name = name
        self.access = access
        self.base_classes = base_classes
        self.body = body
        super().__init__(*args, **kwargs)


class NodeArch(ObjectArch):
    """NodeArch node type for Jac Ast."""


class EdgeArch(ObjectArch):
    """EdgeArch node type for Jac Ast."""


class WalkerArch(ObjectArch):
    """WalkerArch node type for Jac Ast."""


class SpawnerArch(AstNode):
    """SpawnerArch node type for Jac Ast."""

    def __init__(
        self: "SpawnerArch",
        name: AstNode,
        access: AstNode,
        body: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize spawner arch node."""
        self.name = name
        self.access = access
        self.body = body
        super().__init__(*args, **kwargs)


class BaseClasses(AstNode):
    """BaseArch node type for Jac Ast."""

    def __init__(
        self: "BaseClasses", base_classes: list, *args: list, **kwargs: dict
    ) -> None:
        """Initialize base classes node."""
        self.base_classes = base_classes
        super().__init__(*args, **kwargs)


class AbilitySpec(AstNode):
    """AbilitySpec node type for Jac Ast."""

    def __init__(
        self: "AbilitySpec",
        name: AstNode,
        arch: AstNode,
        mod: AstNode,
        signature: AstNode,
        body: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize arch block node."""
        self.name = name
        self.arch = arch
        self.mod = mod
        self.signature = signature
        self.body = body
        super().__init__(*args, **kwargs)


class ArchBlock(AstNode):
    """ArchBlock node type for Jac Ast."""

    def __init__(
        self: "ArchBlock",
        body: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize arch block node."""
        self.body = body
        super().__init__(*args, **kwargs)


class HasStmt(AstNode):
    """HasStmt node type for Jac Ast."""

    def __init__(
        self: "HasStmt",
        access: AstNode,
        vars: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize has statement node."""
        self.access = access
        self.vars = vars
        super().__init__(*args, **kwargs)


class ParamVar(AstNode):
    """ParamVar node type for Jac Ast."""

    def __init__(
        self: "ParamVar",
        name: AstNode,
        type_spec: AstNode,
        value: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize has var node."""
        self.name = name
        self.type_spec = type_spec
        self.value = value
        super().__init__(*args, **kwargs)


class HasVar(ParamVar):
    """HasVar node type for Jac Ast."""

    def __init__(
        self: "HasVar",
        tags: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize has var node."""
        self.tags = tags
        super().__init__(*args, **kwargs)


class HasVarTags(AstNode):
    """HasVarTags node type for Jac Ast."""

    def __init__(
        self: "HasVarTags",
        tags: list,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize has var tags node."""
        self.tags = tags
        super().__init__(*args, **kwargs)


class TypeSpec(AstNode):
    """TypeSpec node type for Jac Ast."""

    def __init__(
        self: "TypeSpec",
        typ: AstNode,
        nested1: AstNode,  # needed for lists
        nested2: AstNode,  # needed for dicts
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize type spec node."""
        self.typ = typ
        self.nested1 = nested1
        self.nested2 = nested2
        super().__init__(*args, **kwargs)


class CanDS(AstNode):
    """CanDS node type for Jac Ast."""

    def __init__(
        self: "CanDS",
        name: AstNode,
        access: AstNode,
        signature: AstNode,
        body: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize can statement node."""
        self.name = name
        self.access = access
        self.signature = signature
        self.body = body
        super().__init__(*args, **kwargs)


class CanMethod(CanDS):
    """CanMethod node type for Jac Ast."""


class EventSignature(AstNode):
    """EventSignature node type for Jac Ast."""

    def __init__(
        self: "EventSignature",
        event: AstNode,
        arch_access: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize event signature node."""
        self.event = event
        self.arch_access = arch_access
        super().__init__(*args, **kwargs)


class MethodSignature(AstNode):
    """MethodSignature node type for Jac Ast."""

    def __init__(
        self: "MethodSignature",
        params: AstNode,
        return_type: AstNode,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize method signature node."""
        self.params = params
        self.return_type = return_type
        super().__init__(*args, **kwargs)


class NameList(AstNode):
    """NameList node type for Jac Ast."""

    def __init__(
        self: "NameList",
        names: list,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize name list node."""
        self.names = names
        super().__init__(*args, **kwargs)


class MethodParams(AstNode):
    """ArchBlock node type for Jac Ast."""

    def __init__(
        self: "MethodParams",
        params: list,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize method params node."""
        self.params = params
        super().__init__(*args, **kwargs)


class CodeBlock(AstNode):
    """CodeBlock node type for Jac Ast."""

    def __init__(
        self: "CodeBlock",
        body: list,
        *args: list,
        **kwargs: dict,
    ) -> None:
        """Initialize code block node."""
        self.body = body
        super().__init__(*args, **kwargs)