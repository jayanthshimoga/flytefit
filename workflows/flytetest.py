from flytekit import task, workflow
from pyathena import connect

@task
def test():
    try:
        access_key = "AKIAQNZ3GR56E7BQ22VF"
        secret_key = "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"

        conn  = connect(aws_access_key_id=access_key,
                           aws_secret_access_key=secret_key,
                           s3_staging_dir="s3://drd-029652062076-28e0/",
                           region_name="us-east-1")
        query = "SELECT * FROM default.flytetestingflytetesting limit 10;"
        cursor = conn.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        conn.close()
        print("Done")
    
    except Exception as e:
        print(e)


@workflow
def hello_world_wf():
    test()
    print("success")


if __name__ == "__main__":
    print(f"Running wf() {hello_world_wf()}")