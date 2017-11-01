import graphene
from institutions.schema import Query as institutions_schema
from students.schema import Query as students_schema


class Query(institutions_schema, students_schema, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
