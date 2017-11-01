import graphene
import institutions.schema as institutions_schema


class Query(institutions_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
