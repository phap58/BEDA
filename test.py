import static.remote.restart as rt
import static.remote.stop as st
import static.remote.process as pr
import static.remote.program as pg
import static.router.infomation as i
import static.remote.sending as sd
import static.router.program as pd2

def test():
    # print(rt.restart_vm_by_id(2,"401"))
    path = i.get_pathvm_by_id_and_room(2,"401")
    # print(path)
    # pr.exce_list_process_in_1vm(path)
    sd.send_file_to_vm(path,1)
    
test()