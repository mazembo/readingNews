import yaml
d = {'A':'a', 'B':{'C':'c', 'D':'d', 'E':'e'}}
print (d)
print len(d)
print type(d)
with open('result.yml', 'w') as yaml_file:
    yaml.dump(d, yaml_file, default_flow_style=False)
