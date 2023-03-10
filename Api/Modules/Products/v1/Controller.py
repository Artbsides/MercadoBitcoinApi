from uuid import UUID
from fastapi import APIRouter, Depends
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

    @router.post("/")
    def create(product: ProductDto, productsService: ProductsService = Depends()) -> object:
        product: Product = productsService.create(product.toModel())

        return {
            "data": product
        }


    @router.get("/")
    def getAll(productsService: ProductsService = Depends()) -> object:
        return {
            "data": productsService.getAll()
        }

    @router.get("/{product_id}")
    def get(product_id: UUID, productsService: ProductsService = Depends()) -> object:
        return {
            "data": productsService.get(product_id)
        }

    @router.patch("/{product_id}")
    def update(product: ProductDto, productsService: ProductsService = Depends()) -> object:
        product: Product = productsService.update(product.toModel())

        return {
            "data": product
        }

    @router.delete("/{product_id}")
    def delete(product_id: UUID, productsService: ProductsService = Depends()) -> object:
        return productsService.delete(product_id)
