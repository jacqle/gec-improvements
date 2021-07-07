# File used to pipe the different components of the GEC system
# Each component must take a input file, and output a modified file

import argparse
import os
import subprocess

workdir = os.path.dirname(__file__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--pipeline',
                        help='Elements of the pipeline, to be applied sequentially',
                        nargs="+",
                        required=True)
                        
    args = parser.parse_args()
    pipes = args.pipeline

    # Creates results folder
    folder_id = 1
    while os.path.exists(f"{workdir}/{folder_id}/"):
        folder_id += 1

    output_folder = f"{workdir}/{folder_id}/"
    os.mkdir(output_folder)

    orig_file = os.path.join(workdir, "../../data/conll14st-test-data/origin_corpus.txt")

    file_history = [orig_file]

    # include tests for the pipe order

    # piping the input file
    for i, pipe in enumerate(pipes):
        run_pipe_file = os.path.join(workdir, f"../{pipe}/run_pipe.py")
        if not os.path.isfile(run_pipe_file):
            print(f"Could not load pipe {pipe}.")
            print("Make sure the directory exists, and that it contains a run_pipe.py file.")
            raise(ValueError)

        print(f"Running pipe {pipe}...")

        new_file = f"{output_folder}"+"_".join([p for p in pipes[:i+1]])+".txt"
        # running the pipe
        subprocess.run(f"python {run_pipe_file} --input {file_history[-1]} --output {new_file}", shell=True, check=True)

        file_history.append(new_file)

    gold_m2 = os.path.join(workdir,"../../data/conll14st-test-data/gold.m2")
    out_m2 = f"{output_folder}"+"_".join([p for p in pipes])+".m2"

    # running errant parallel between orig file and corrected file
    subprocess.run(f"errant_parallel -orig {orig_file} -cor {file_history[-1]}  -out {out_m2}", shell=True, check=True)

    print("\nComputing difference between hyp m2 and gold m2... ")
    # running errant score between hypothetical m2 and gold m2
    subprocess.run(f"errant_compare -hyp {out_m2} -ref {gold_m2} > {output_folder}result.txt", shell=True, check=True)

    print(f"\nPipeline succesfully executed. \n See results in {output_folder}")