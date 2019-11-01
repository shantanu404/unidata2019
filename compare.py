import os
import argparse

RESULTS = dict()
INSTITUITIONS = ['buet', 'iut', 'kuet']

def get_result(filename):
  res = dict()
  with open(filename) as f:
    for line in f:
      words = line.split(',')
      name = words[1]
      merit = int(words[2])
      if name in res:
        res[name] = max(merit, res[name])
      res[name] = merit
  return res

for inst in INSTITUITIONS:
  filename = os.path.dirname(os.path.realpath(__file__)) + '/data/{}.csv'
  RESULTS[inst] = get_result(filename.format(inst))

def lagging(name, target_inst, other_inst, cutoff=500):
  name = name.upper()

  if target_inst not in INSTITUITIONS or other_inst not in INSTITUITIONS:
    raise ValueError('{} not in acquired data.'.format(target_inst))
  try:
    target_inst_merit = RESULTS[target_inst][name]
  except KeyError:
    raise ValueError('{} not found in {}'.format(name, target_inst))

  names = []
  for student, merit in RESULTS[other_inst].items():
    try:
      if merit <= cutoff and RESULTS[target_inst][student] < target_inst_merit:
        names.append(student)
    except KeyError:
      pass

  return names

def main():
  parser = argparse.ArgumentParser(
    description='Finds the students above your position who got chance in other instituitions')
  parser.add_argument('name', type=str, help='Your name to find your merit')
  parser.add_argument('target', type=str, help='Your target college')
  parser.add_argument('other', type=str, help='College to check meritlist of')
  parser.add_argument('-c', '--cutoff', dest='cutoff', action='store', default=500, type=int,
                      help='Specify the other institutes\'s possible cuttoff position')
  parser.add_argument('-s', '--showall', dest='showall', action='store_true')

  args = parser.parse_args()

  names = lagging(args.name, args.target, args.other, args.cutoff)
  if args.showall:
    print('\n'.join(names))
  print('There are {} who are before {} in {} but in top {} @ {}'.format(
    len(names), args.name, args.target, args.cutoff, args.other
  ))

if __name__ == '__main__':
  main()