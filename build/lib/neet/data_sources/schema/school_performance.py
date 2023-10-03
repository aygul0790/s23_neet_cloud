from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

_schema = DataFrameSchema(
    columns={
        "estab": Column(
            dtype="Int64",
            nullable=False,
            unique=True,
            description=None,
            title=None,
        ),
        "perctot": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0),
                Check.less_than_or_equal_to(max_value=100.0),
            ],
            nullable=True,
            description=None,
            title=None,
        ),
        "pnorg": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=100.0),
            ],
            nullable=True,
            description=None,
            title=None,
        ),
        "psenelk": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=100),
            ],
            nullable=True,
            description=None,
            title=None,
        ),
        "pnumengfl": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=100.0),
            ],
            nullable=True,
            description=None,
            title=None,
        ),
        "norfsmever": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=0.0),
                Check.less_than_or_equal_to(max_value=100000.0),
            ],
            nullable=True,
            description=None,
            title=None,
        ),
        "postcode": Column(
            dtype="category",
            checks=None,
            nullable=True,
            description=None,
            title=None,
        ),
        "schooltype_y": Column(
            dtype="category",
            nullable=True,
            description=None,
            title=None,
        ),
        "gender": Column(
            dtype="category",
            checks=[Check.isin(allowed_values=["Mixed", "Boys", "Girls"])],
            nullable=True,
            description=None,
            title=None,
        ),
        "ofstedrating": Column(
            dtype="category",
            checks=[
                Check.isin(
                    allowed_values=[
                        "Outstanding",
                        "Good",
                        "Requires improvement",
                        "Inadequate",
                        "Serious Weaknesses",
                        "Special Measures",
                    ]
                )
            ],
            nullable=True,
            description=None,
            title=None,
        ),
        "ofstedlastinsp": Column(
            dtype="object",
            checks=None,
            nullable=True,
            description=None,
            title=None,
        ),
    },
    coerce=True,
    strict="filter",
    name="la_schools",
    ordered=False,
    report_duplicates="all",
    unique_column_names=True,
    add_missing_columns=False,
    title="LA school data",
    description="Addtional data about each school in the local authority.",
)
