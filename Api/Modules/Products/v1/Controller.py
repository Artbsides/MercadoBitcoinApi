from uuid import UUID
from http import HTTPStatus
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

    @router.post("/", status_code = HTTPStatus.CREATED)
    def create(product: ProductDto, productsService: ProductsService = Depends()) -> dict:
        product: Product = productsService.create(product.toModel())

        return {
            "data": product
        }


    @router.get("/")
    def getAll(productsService: ProductsService = Depends()) -> dict:
        return {
            "data": productsService.getAll()
        }

    @router.get("/{product_id}")
    def get(product_id: UUID, productsService: ProductsService = Depends()) -> dict:
        return {
            "data": productsService.get(product_id)
        }

    @router.patch("/{product_id}", status_code = HTTPStatus.NO_CONTENT)
    def update(product_id: UUID, product: ProductDto, productsService: ProductsService = Depends()) -> None:
        productsService.update(product.toModel(product_id))

    @router.delete("/{product_id}", status_code = HTTPStatus.NO_CONTENT)
    def delete(product_id: UUID, productsService: ProductsService = Depends()) -> None:
        productsService.delete(product_id)
