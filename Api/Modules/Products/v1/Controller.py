from fastapi import APIRouter, Body, Depends
from Api.Modules.Products.v1.Dtos.Product import ProductDto
from Api.Modules.Products.v1.Models.Product import Product
from Api.Modules.Products.v1.Service import ProductsService


class ProductsController:
    router = APIRouter(
        tags=[
            "Products"
        ],
        prefix="/products"
    )

    @router.get("/{product_id}")
    def get(product_id: str, productsService: ProductsService = Depends()) -> object:
        return {
            "data": productsService.get(product_id)
        }

    @router.get("/")
    def getAll(productsService: ProductsService = Depends()) -> object:
        return {
            "data": productsService.getAll()
        }

    @router.post("/")
    def create(product: ProductDto, productsService: ProductsService = Depends()) -> object:
        product: Product = productsService.create(product.toModel())

        return {
            "data": product
        }
