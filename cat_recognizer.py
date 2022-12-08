class CatRecognizer:
    """
    Interface for checking if the image contains a cat
    """

    def is_cat(self, image_path: str) -> bool:
        """
        Checks if image stored in image_path file contains a cat

        This method should be implemented in subclasses

        Args:
            image_path: path to the image to be checked

        Returns:
            True if the image contains a cat
        """
        raise NotImplementedError
