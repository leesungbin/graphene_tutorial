from graphene import relay, ObjectType, AbstractType, String
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ingredients.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(object):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)


class CategoryCreate(relay.ClientIDMutation):
    category = relay.Node.Field(CategoryNode)

    class Input:
        name = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, client_mutation_id=None):
        category = Category(name=name)
        category.save()
        return CategoryCreate(category=category)


class CategoryDelete(relay.ClientIDMutation):
    category = relay.Node.Field(CategoryNode)

    class Input:
        id = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, client_mutation_id=None):
        category = Category.objects.get(id=id)
        category.delete()
        return CategoryDelete(ok=True)


class RelayMutation(AbstractType):
    category_create = CategoryCreate.Field()
    category_delete = CategoryDelete.Field()
