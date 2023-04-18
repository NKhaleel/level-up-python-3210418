import time
import sched


def schedule_function(time_to_run, fun, *fun_inputs):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(time_to_run, 1, fun, argument=fun_inputs)
    print("Will run " + str(fun.__name__) +
          " at " + str(time.ctime(time_to_run)))
    s.run()
