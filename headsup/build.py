# game.src.html + images/*.jpg -> self-contained index.html
import base64, pathlib
d = pathlib.Path(__file__).parent
imgs = ",".join(f'{i}:"data:image/jpeg;base64,{base64.b64encode((d/"images"/f"{i}.jpg").read_bytes()).decode()}"' for i in range(1, 18))
(d/"index.html").write_text((d/"game.src.html").read_text().replace("/*IMGS*/", imgs))
