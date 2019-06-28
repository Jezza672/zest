all_tests = []


def test(obj):
    return obj.__test__()

def test_all():
    from .results import Results

    out = Results(f"All {len(all_tests)} tests:")
    print(len(all_tests))
    for te in all_tests:
        out.append(test(te))
    return out