# Evidence of Demand: Researcher Survey Summary

As part of validating the problem space and the willingness-to-pay (WTP) for the **AutoData-Refiner** system, we conducted mini-interviews with three active researchers working in university computer vision and autonomous vehicle laboratories. This document summarizes the questions asked and the qualitative insights gathered.

## Interview Setup
* **Target Audience:** Researchers, Graduate Students, and Ph.D. candidates focusing on deep learning, computer vision, and autonomous vehicle perception.
* **Sample Size:** 3 participants.
* **Goal:** To confirm whether the bottleneck in processing open-source driving datasets is significant enough to justify a paid, on-demand refinement service.

---

## Survey Questions

1.  **Workflow & Tooling:** What open-source driving datasets (e.g., KITTI, Waymo, nuScenes) do you use most frequently, and what is your typical process for downloading and ingesting them locally?
2.  **Pain Points:** What are the most significant bottlenecks or frustrations you face when preparing this raw data for your specific research tasks?
3.  **Time & Storage Cost:** Approximately how much engineering time and local storage space do you spend filtering, cleaning, or extracting specific edge cases (e.g., "rainy night scenes with pedestrians") before you can actually begin training your models?
4.  **Willingness to Pay:** If there were a service that provided on-demand, pre-filtered, and downsized subsets tailored perfectly to your specific scenario parameters, would your lab be willing to pay for it? If so, what pricing model makes sense to you?

---

## Summary of Responses

### Researcher A (Ph.D. Candidate, AV Perception Lab)
* **Workflow:** Relies heavily on the Waymo Open Dataset. Usually writes custom Python bash scripts to fetch chunks of data overnight.
* **Pain Points:** Constantly runs into local disk space limits. The dataset is multiple terabytes, but they often only need scenes with rare weather conditions (like heavy rain or fog) for robustness testing.
* **Time & Cost:** Estimates that **70% of project initialization time** is purely wasted on waiting for downloads and running local masks to delete irrelevant scenes.
* **WTP:** Highly enthusiastic. Stated they would gladly pay for a service using their lab's cloud computing budget if it could save them days of manual scripting and free up local NAS storage. 

### Researcher B (Research Assistant, Computer Vision Group)
* **Workflow:** Uses KITTI and nuScenes. Often has to download the entire multi-modal package (LiDAR, Radar, all 6 cameras).
* **Pain Points:** Network throttling from official academic mirrors is a massive headache. Also, they frequently only need specific sensor streams (e.g., only front-facing camera + LiDAR, completely ignoring side cameras), but the raw data packages force them to download everything.
* **Time & Cost:** Valued their own engineering time spent on "data wrangling" at roughly $15 USD/hour. A complex extraction task can easily take 15–20 hours per project.
* **WTP:** Mentioned that a "Pay-Per-Gigabyte" output model makes the most sense because it is transparent and easy to justify on a lab expense report as an infrastructure cost.

### Researcher C (Master's Student, Intelligent Vehicles Lab)
* **Workflow:** Primarily works with proprietary and mixed open-source sets for pedestrian detection. 
* **Pain Points:** The biggest issue is writing custom data-loaders and filtering scripts for every single new project. The code is rarely reusable because data formats differ.
* **Time & Cost:** It takes them 2–3 days of manual coding and debugging just to get a clean subset ready for their PyTorch pipeline.
* **WTP:** Expressed strong willingness to subscribe to a platform, provided that **data integrity** (bounding box coordinates perfectly matching the filtered frames) is strictly maintained. They emphasized that if the tool corrupts the annotations, it's useless.
