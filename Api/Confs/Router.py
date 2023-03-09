from fastapi import APIRouter
from Api.Modules.Products.v1.Controller import ProductsController


router = APIRouter()
router.include_router(ProductsController.router)
