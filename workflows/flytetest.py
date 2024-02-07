from flytekit import task, workflow
from pyathena import connect
from pyathena.pandas.cursor import PandasCursor
import traceback
    

@task
def test1():
    try:
        access_key = ""
        secret_key = ""
        conn  = connect(aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            s3_staging_dir="",
                            region_name="us-east-1",
                            cursor_class=PandasCursor).cursor()
        query = "SELECT * FROM default.flytetestingflytetesting limit 10;"
        conn.execute(query)
        print("query is executed")
    except Exception:
        print(traceback.format_exc())

@workflow
def hello_world_wf():
    test1()
    print("success")


if __name__ == "__main__":
    print(f"Running wf() {hello_world_wf()}")