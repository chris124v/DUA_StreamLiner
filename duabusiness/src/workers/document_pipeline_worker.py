class DocumentPipelineWorker:
    def run(self) -> None:
        raise NotImplementedError("Contract only")

if __name__ == "__main__":
    DocumentPipelineWorker().run()

