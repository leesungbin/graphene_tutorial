import graphene
import ingredients.schema


class Query(ingredients.schema.Query, graphene.ObjectType):
    pass


class Mutation(ingredients.schema.RelayMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
