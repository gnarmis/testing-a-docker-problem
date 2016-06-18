import hug

@hug.post('/docker-test')
def docker_test():
  return "Hey there, I'm supposedly running on the host!"
