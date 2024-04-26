from typing import Any, Generic, Type, TypeVar
from uuid import UUID

from pydantic import BaseModel

from src.database import Base
from src.repositories import BaseRepository
from src.utils.exceptions import NotFoundException

ModelType = TypeVar("ModelType", bound=Base)


class BaseController(Generic[ModelType]):
    """Base class for data controllers."""

    def __init__(self, model: Type[ModelType], repository: BaseRepository):
        self.model_class = model
        self.repository = repository

    def get_by_id(self, id_: int, join_: set[str] | None = None) -> ModelType:
        """
        Returns the model instance matching the id.

        :param id_: The id to match.
        :param join_: The joins to make.
        :return: The model instance.
        """

        db_obj = self.repository.get_by(
            field="id", value=id_, join_=join_, unique=True
        )
        if not db_obj:
            raise NotFoundException(
                message=(
                    f"{self.model_class.__tablename__.title()} "
                    f"with id: {id} does not exist"
                )
            )

        return db_obj

    def get_by_uuid(
        self, uuid: UUID, join_: set[str] | None = None
    ) -> ModelType:
        """
        Returns the model instance matching the uuid.

        :param uuid: The uuid to match.
        :param join_: The joins to make.
        :return: The model instance.
        """

        db_obj = self.repository.get_by(
            field="uuid", value=uuid, join_=join_, unique=True
        )
        if not db_obj:
            raise NotFoundException(
                message=(
                    f"{self.model_class.__tablename__.title()} "
                    f"with id: {uuid} does not exist"
                )
            )
        return db_obj

    def get_one(
        self, conditions: dict[str | Any]
    ) -> ModelType | None:
        return self.repository.get_one(conditions)

    def get_all(
        self, conditions: dict[str | Any], skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        """
        Returns a list of records based on pagination params.

        :param skip: The number of records to skip.
        :param limit: The number of records to return.
        :param join_: The joins to make.
        :return: A list of records.
        """
        return self.repository.get_all(conditions, skip, limit)

    def create(self, attributes: dict[str, Any]) -> ModelType:
        """
        Creates a new Object in the DB.

        :param attributes: The attributes to create the object with.
        :return: The created object.
        """
        create = self.repository.create(attributes)
        return create

    def delete(self, model: ModelType) -> bool:
        """
        Deletes the Object from the DB.

        :param model: The model to delete.
        :return: True if the object was deleted, False otherwise.
        """
        delete = self.repository.delete(model)
        return delete

    @staticmethod
    def extract_attributes_from_schema(
        schema: BaseModel, excludes: set = None
    ) -> dict[str, Any]:
        """
        Extracts the attributes from the schema.

        :param schema: The schema to extract the attributes from.
        :param excludes: The attributes to exclude.
        :return: The attributes.
        """

        return schema.dict(exclude=excludes, exclude_unset=True)
