from jsonschema import validate


def validate_schema(instance: dict, schema: dict) -> None:
    validate(instance=instance, schema=schema)