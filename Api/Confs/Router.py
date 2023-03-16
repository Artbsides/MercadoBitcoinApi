from fastapi import APIRouter

from Api.Modules.Products.v1.Controller import ProductsController \
  as ProductsControllerV1


router = APIRouter()
router.include_router(ProductsControllerV1.router)
