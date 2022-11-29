# generated by datamodel-codegen:
#   filename:  confluent-cloud-api.spec.json
#   timestamp: 2022-11-29T07:24:39+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra

from . import ApiVersion, Id, Kind, ResourceMetadata, SpecElement


class Spec(BaseModel):
    class Config:
        extra = Extra.forbid

    display_name: Optional[str] = None
    description: Optional[str] = None
    secret: Optional[str] = None
    owner: Optional[SpecElement] = None
    resource: Optional[SpecElement] = None


class SpecModel(BaseModel):
    class Config:
        extra = Extra.forbid

    api_version: Optional[ApiVersion] = None
    id: Optional[Id] = None
    kind: Optional[Kind] = None
    metadata: Optional[ResourceMetadata] = None
    spec: Optional[Spec] = None
