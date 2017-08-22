import graphene
import ingredients.schema

# Project level query - what exactly does it do?
class Query(ingredients.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
