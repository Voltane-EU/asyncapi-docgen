from typing import Optional, List, Dict, Any, Union, Literal
from pydantic import BaseModel, Field, AnyUrl, EmailStr


class Reference(BaseModel):
    ref: str = Field(alias="$ref")


class Contact(BaseModel):
    name: Optional[str]
    url: Optional[AnyUrl]
    email: Optional[EmailStr]


class License(BaseModel):
    name: str
    url: Optional[AnyUrl]


class Info(BaseModel):
    title: str
    version: str
    description: Optional[str]
    termsOfService: Optional[AnyUrl]
    contact: Optional[Contact]
    license: Optional[License]


class ServerVariable(BaseModel):
    enum: Optional[List[str]]
    default: Optional[str]
    description: Optional[str]
    examples: Optional[List[str]]

    class Config:
        extra = 'allow'


class SecurityScheme(BaseModel):
    type: Literal['userPassword', 'apiKey', 'X509', 'symmetricEncryption', 'asymmetricEncryption', 'httpApiKey', 'http', 'oauth2', 'openIdConnect']
    description: Optional[str]
    name: Optional[str]
    in_: Optional[str] = Field(default=None, alias='in')
    scheme: Optional[str]
    bearerFormat: Optional[str]
    flows: Optional[str]
    openIdConnectUrl: Optional[str]

    class Config:
        extra = 'allow'


class Server(BaseModel):
    url: str
    protocol: str
    protocolVersion: Optional[str]
    description: Optional[str]
    variables: Optional[Dict[str, ServerVariable]]
    security: Optional[Dict[str, List[str]]]
    bindings: Optional[Any]  # TODO


class ExternalDocumentation(BaseModel):
    url: AnyUrl
    description: Optional[str]


class Tag(BaseModel):
    name: str
    description: Optional[str]
    externalDocs: Optional[ExternalDocumentation]


class SchemaBase(BaseModel):
    ref: Optional[str] = Field(None, alias="$ref")
    title: Optional[str] = None
    multipleOf: Optional[float] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[float] = None
    maxLength: Optional[int] = Field(None, gte=0)
    minLength: Optional[int] = Field(None, gte=0)
    pattern: Optional[str] = None
    maxItems: Optional[int] = Field(None, gte=0)
    minItems: Optional[int] = Field(None, gte=0)
    uniqueItems: Optional[bool] = None
    maxProperties: Optional[int] = Field(None, gte=0)
    minProperties: Optional[int] = Field(None, gte=0)
    required: Optional[List[str]] = None
    enum: Optional[List[Any]] = None
    type: Optional[str] = None
    allOf: Optional[List[Any]] = None
    oneOf: Optional[List[Any]] = None
    anyOf: Optional[List[Any]] = None
    not_: Optional[Any] = Field(None, alias="not")
    items: Optional[Any] = None
    properties: Optional[Dict[str, Any]] = None
    additionalProperties: Optional[Union[Dict[str, Any], bool]] = None
    description: Optional[str] = None
    format: Optional[str] = None
    default: Optional[Any] = None
    nullable: Optional[bool] = None
    readOnly: Optional[bool] = None
    writeOnly: Optional[bool] = None
    externalDocs: Optional[ExternalDocumentation] = None
    example: Optional[Any] = None
    deprecated: Optional[bool] = None


class Schema(SchemaBase):
    allOf: Optional[List[SchemaBase]] = None
    oneOf: Optional[List[SchemaBase]] = None
    anyOf: Optional[List[SchemaBase]] = None
    not_: Optional[SchemaBase] = Field(None, alias="not")
    properties: Optional[Dict[str, SchemaBase]] = None
    additionalProperties: Optional[Union[Dict[str, Any], bool]] = None


class CorrelationId(BaseModel):
    description: Optional[str]
    location: str


class _Message(BaseModel):
    headers: Optional[Union[Reference, Schema]]
    correlationId: Optional[Union[Reference, CorrelationId]]
    schemaFormat: Optional[str]
    contentType: Optional[str]
    name: Optional[str]
    title: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    tags: Optional[List[Tag]]
    externalDocs: Optional[ExternalDocumentation]
    bindings: Optional[Any]  # TODO
    examples: Optional[Dict[str, Any]]


class MessageTrait(_Message):
    pass


class Message(_Message):
    payload: Union[Reference, Schema, Any]
    traits: Optional[List[MessageTrait]]


class _Operation(BaseModel):
    operationId: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    tags: Optional[List[Tag]]
    externalDocs: Optional[ExternalDocumentation]
    bindings: Optional[Any]  # TODO


class OperationTrait(_Operation):
    pass


class Operation(_Operation):
    traits: Optional[List[OperationTrait]]
    message: Optional[Message]


class Parameter(BaseModel):
    description: Optional[str]
    schema_: Optional[Schema] = Field(default=None, alias='schema')
    location: Optional[str]


class Channel(BaseModel):
    ref: Optional[str] = Field(default=None, alias='$ref')
    description: Optional[str]
    subscribe: Optional[Operation]
    publish: Optional[Operation]
    parameters: Optional[Dict[str, Parameter]]
    bindings: Optional[Any]  # TODO


class Components(BaseModel):
    schemas: Optional[Dict[str, Schema]]
    messages: Optional[Dict[str, Message]]
    securitySchemes: Optional[Dict[str, SecurityScheme]]
    parameters: Optional[Dict[str, Parameter]]
    correlationIds: Optional[Dict[str, CorrelationId]]
    operationTraits: Optional[Dict[str, OperationTrait]]
    messageTraits: Optional[Dict[str, MessageTrait]]
    serverBindings: Optional[Dict[str, Any]]  # TODO
    channelBindings: Optional[Dict[str, Any]]  # TODO
    operationBindings: Optional[Dict[str, Any]]  # TODO
    messageBindings: Optional[Dict[str, Any]]  # TODO


class AsyncAPI(BaseModel):
    asyncapi: str
    id: Optional[AnyUrl]
    info: Info
    servers: Optional[Dict[str, Server]]
    channels: Dict[str, Channel]
    components: Optional[Components]
    tags: Optional[List[Tag]]
    externalDocs: Optional[ExternalDocumentation]
