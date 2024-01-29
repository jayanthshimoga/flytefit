# from math import sqrt
# from flytekit import task, workflow, mean, LaunchPlan
# from typing import List


# @task
# def standard_deviation(values: List[float], mu: float) -> float:
#     variance = sum([(x - mu) ** 2 for x in values])
#     return sqrt(variance)

# @task
# def standard_scale(values: List[float], mu: float, sigma: float) -> List[float]:
#     return [(x - mu) / sigma for x in values]


# @workflow
# def standard_scale_workflow(values: List[float]) -> List[float]:
#     mu = mean(values=values)
#     sigma = standard_deviation(values=values, mu=mu)
#     return standard_scale(values=values, mu=mu, sigma=sigma)

# # standard_scale_launch_plan = LaunchPlan.get_or_create(
# #     standard_scale_workflow,
# #     name="standard_scale_lp",
# #     default_inputs={"values": [3.0, 4.0, 5.0]}
# # )
# if __name__ == "__main__":
#     print(f"Running wf() {standard_scale_workflow(values=[4.0, 5.6, 7.1, 8.2])}")