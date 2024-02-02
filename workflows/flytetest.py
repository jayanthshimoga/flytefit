from flytekit import task, workflow
from pyathena import connect
from pyathena.pandas.cursor import PandasCursor


@task
def test1():

    # Please use your access key,secret key and aws output bucket for your athena query
    access_key = ""
    secret_key = ""
    conn  = connect(aws_access_key_id=access_key,
                           aws_secret_access_key=secret_key,
                           s3_staging_dir="",
                           region_name="us-east-1",
                           cursor_class=PandasCursor).cursor()
    query = "SELECT * FROM default.flytetestingflytetesting limit 10;"
    df = conn.execute(query).as_pandas()
    print(df.head(5))

@workflow
def hello_world_wf():
    test1()
    print("success")


if __name__ == "__main__":
    print(f"Running wf() {hello_world_wf()}")