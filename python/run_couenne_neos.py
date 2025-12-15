import xmlrpc.client, time
from pathlib import Path

def run_couenne_neos(mod_file, email, poll=5, timeout=300):
    model = Path(mod_file).read_text()
    neos = xmlrpc.client.ServerProxy("https://neos-server.org:3333")

    xml = f"""
<MyProblem>
  <category>minco</category>
  <solver>Couenne</solver>
  <inputType>AMPL</inputType>
  <email>{email}</email>
        <model><![CDATA[{model}]]></model>
<data><![CDATA[]]></data>
</MyProblem>
        """.strip()

    job, pwd = neos.submitJob(xml)
    assert job > 0, "NEOS submission failed"
    print(f"Couenne job {job}")

    t0 = time.time()
    while neos.getJobStatus(job, pwd) != "Done":
        if time.time() - t0 > timeout:
            raise RuntimeError("Couenne timeout")
        time.sleep(poll)

    return neos.getFinalResults(job, pwd).data.decode()    
