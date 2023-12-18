from typing import Annotated, Dict, Hashable, List, Optional, Union

DocumentKeyType = Hashable
DocumentValueType = Optional[
    Union[
        Annotated[Dict, "object in a json document"],
        Annotated[List, "array in a json document"],
        DocumentKeyType,
    ]
]
DocumentObjectType = Annotated[
    Dict[DocumentKeyType, DocumentValueType], "object in a json document"
]
DocumentArrayType = Annotated[List[DocumentValueType], "array in a json document"]

DocumentType = Union[DocumentObjectType, DocumentArrayType]
