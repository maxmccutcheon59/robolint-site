"""Generates the audit results table rows from AUDIT.md data (copied verbatim) into docs/index.html."""
rows = [
("EPITECH-LILLE/eval_training",60,36.6,"F","20 (33%)","merged recordings, metadata says 0 episodes","real"),
("kmg0620/so101_bomb_pick_place_v1",150,55.3,"F","22 (15%)","merged recordings, 47 episodes missing from metadata","real"),
("jchandru08/so100_press_red_button",29,55.5,"F","7 (24%)","metadata/data mismatch, missing episodes","real"),
("SO-101-robot-learning/so101_pick_place",50,78.5,"C","0","metadata says 0 episodes","real"),
("imstevenpmwork/omx_sentry_1",7,82.0,"B","0","no task description","real"),
("lerobot/svla_so100_stacking",56,90.8,"A","5 (9%)","dead and false-start episodes","real"),
("Embodied-AI-6/dataset",160,91.0,"A","0","33% of all frames are idle","real"),
("lerobot/svla_so100_sorting",52,96.2,"A","2 (4%)","dead episodes","real"),
("lerobot/aloha_sim_transfer_cube_scripted",50,98.5,"A","0","near-identical scripted demos","sim"),
("lerobot/svla_so101_pickplace",50,98.7,"A","0","idle padding","real"),
("lerobot/svla_so100_pickplace",50,98.9,"A","0","idle padding","real"),
("brandonyang/artem-pour-water",1445,99.8,"A","0","22 single-frame tracking glitches","real"),
("lerobot/pusht",206,100,"A","0","none","sim"),
("lerobot/aloha_sim_transfer_cube_human",50,100,"A","0","none","sim"),
("lerobot/aloha_sim_insertion_human",50,100,"A","0","none","sim"),
("lerobot/aloha_sim_insertion_scripted",50,100,"A","0","none","sim"),
("lerobot/libero",1693,100,"A","0","2 minor glitches","sim"),
("recast-robotics/rollout_dagger_r1_s2_b0_20260915_121327",10,100,"A","0","none","und"),
]
assert sum(r[1] for r in rows) == 4218 and len(rows) == 18
kinds = {"real":("k-real","Real robot"),"sim":("k-sim","Simulation"),"und":("k-und","Not documented")}
out = []
for ds,ep,sc,gr,err,issue,k in rows:
    cls = "low" if sc < 70 else ("mid" if sc < 90 else "")
    s = ("100" if sc == 100 else f"{sc:.1f}")
    w = "w" + s.replace(".","_")
    kc,kl = kinds[k]
    out.append(f'          <tr><td class="ds"><a href="https://huggingface.co/datasets/{ds}" rel="noopener noreferrer" target="_blank">{ds}</a></td>'
               f'<td><span class="kind {kc}">{kl}</span></td><td class="num">{ep:,}</td>'
               f'<td><span class="bar {cls}"><i class="{w}"></i><b>{s} ({gr})</b></span></td>'
               f'<td class="num">{err}</td><td>{issue}</td></tr>')
html = open("docs/index.html").read()
start, end = "<!-- ROWS:START -->", "<!-- ROWS:END -->"
a, b = html.index(start) + len(start), html.index(end)
html = html[:a] + "\n" + "\n".join(out) + "\n          " + html[b:]
open("docs/index.html","w").write(html)
print("rows:", len(out))
