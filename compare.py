import os
import argparse

RESULTS = dict()
INSTITUITIONS = ['buet', 'iut', 'kuet', 'cuet', 'ruet',
                 'medical', 'dental', 'sust',
                 'mist-general', 'mist-freedom', 'mist-military', 'mist-tribal']

def get_result(filename):
  res = dict()
  with open(filename) as f:
    for line in f:
      words = line.split(',')
      name = words[1]
      merit = int(words[2])
      if name in res:
        res[name] = min(merit, res[name])
      else:
        res[name] = merit
  return res

for inst in INSTITUITIONS:
  filename = os.path.dirname(os.path.realpath(__file__)) + '/data/{}.csv'
  RESULTS[inst] = get_result(filename.format(inst))

def lagging(tgt_merit, target_inst, other_inst, cutoff=500):
  if target_inst not in INSTITUITIONS or other_inst not in INSTITUITIONS:
    raise ValueError('{} not in acquired data.'.format(target_inst))

  names = []
  for student, merit in RESULTS[other_inst].items():
    try:
      if merit <= cutoff and RESULTS[target_inst][student] < tgt_merit:
        names.append(student)
    except KeyError:
      pass

  return names

def main():
  parser = argparse.ArgumentParser(
    description='Finds the students above your position who got chance in other instituitions')
  parser.add_argument('merit', type=int, help='Your merit position in your target institute')
  parser.add_argument('target', type=str, help='Your target college')
  parser.add_argument('other', type=str, help='College to check meritlist of')
  parser.add_argument('-c', '--cutoff', dest='cutoff', action='store', default=500, type=int,
                      help='Specify the other institutes\'s possible cuttoff position')
  parser.add_argument('-s', '--showall', dest='showall', action='store_true')

  args = parser.parse_args()

  names = lagging(args.merit, args.target, args.other, args.cutoff)
  if args.showall:
    print('\n'.join(names))
  print('There are {} who are before you in {} but in top {} @ {}'.format(
    len(names), args.target, args.cutoff, args.other
  ))

if __name__ == '__main__':
  main()
