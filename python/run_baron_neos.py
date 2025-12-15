import os
import time
import xmlrpc.client
from pathlib import Path


def run_baron_neos(mod_file, email, poll=5, timeout=300):
    model = Path(mod_file).read_text()
    neos = xmlrpc.client.ServerProxy("https://neos-server.org:3333")

    xml = f"""
<MyProblem>
<category>minco</category>
<solver>BARON</solver>
<inputType>AMPL</inputType>
<email>{email}</email>
<model><![CDATA[{model}]]></model>
<data><![CDATA[]]></data>
</MyProblem>
    """.strip()

    job, pwd = neos.submitJob(xml)
    assert job > 0, "NEOS submission failed"
    print(f"BARON job {job} ({os.path.basename(mod_file)})")

    t0 = time.time()
    while neos.getJobStatus(job, pwd) != "Done":
        if time.time() - t0 > timeout:
            raise RuntimeError("BARON timeout")
        time.sleep(poll)

    return neos.getFinalResults(job, pwd).data.decode()


def batch_run_baron_neos(models_dir, log_output, email, poll=5, timeout=300):
    with open(log_output, "w") as out:
        for fname in sorted(os.listdir(models_dir)):
            if not fname.endswith(".mod"):
                continue

            mod_path = os.path.join(models_dir, fname)

            out.write("===================================================\n")
            out.write(f"MODEL: {fname}\n")
            out.write("===================================================\n\n")

            try:
                baron_log = run_baron_neos(
                    mod_path,
                    email,
                    poll=poll,
                    timeout=timeout
                )
                out.write(baron_log)
            except Exception as e:
                out.write(f"ERROR running BARON on {fname}:\n{e}\n")

            out.write("\n\n")

    print("Saved BARON batch log")


def single_run_baron_neos(model, log_output, email, poll=5, timeout=300):
    with open(log_output, "w") as out:
        out.write("===================================================\n")
        out.write(f"MODEL: {os.path.basename(model)}\n")
        out.write("===================================================\n\n")

        try:
            baron_log = run_baron_neos(
                model,
                email,
                poll=poll,
                timeout=timeout
            )
            out.write(baron_log)
        except Exception as e:
            out.write(f"ERROR running BARON on {model}:\n{e}\n")

    print("Saved BARON log")
    