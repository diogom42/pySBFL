from Spectrum import Spectrum


def main():
    spect = Spectrum("", "45-A", "45-A-bug-9385104-9385119")
    print(spect.metrics[1])

if __name__ == "__main__":
    main()