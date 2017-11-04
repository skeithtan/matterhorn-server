import graphene
from institutions.schema import Query as institutions_schema
from students.schema import Query as student_schema


class Query(institutions_schema, student_schema, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, auto_camelcase=False)
