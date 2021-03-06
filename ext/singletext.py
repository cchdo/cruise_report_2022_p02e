import codecs
from os import path

from docutils.io import StringOutput

from sphinx.util import logging
from sphinx.util.console import bold, darkgreen, brown
from sphinx.util.nodes import inline_all_toctrees
from sphinx.util.osutil import ensuredir, os_path
from sphinx.builders.text import TextBuilder
from sphinx.writers.text import TextWriter, TextTranslator

logger = logging.getLogger(__name__)

class SingleFileTextTranslator(TextTranslator):
    def visit_start_of_file(self, node):
        pass
    def depart_start_of_file(self, node):
        pass

class SingleFileTextWriter(TextWriter):
    def translate(self):
        visitor = SingleFileTextTranslator(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = visitor.body

class SingleFileTextBuilder(TextBuilder):
    """
    A TextBuilder subclass that puts the whole document tree in one text file.
    """
    name = 'singletext'
    copysource = False

    def get_outdated_docs(self):
        return 'all documents'

    def assemble_doctree(self):
        master = self.config.master_doc
        tree = self.env.get_doctree(master)
        tree = inline_all_toctrees(self, set(), master, tree, darkgreen, [])
        tree['docname'] = master
        self.env.resolve_references(tree, master, self)
        return tree

    def prepare_writing(self, docnames):
        self.writer = SingleFileTextWriter(self)

    def write(self, *ignored):
        docnames = self.env.all_docs

        logger.info(bold('preparing documents... '))
        self.prepare_writing(docnames)
        logger.info('done')

        logger.info(bold('assembling single document... '))
        doctree = self.assemble_doctree()
        logger.info("")
        logger.info(bold('writing... '))
        self.write_doc(self.config.master_doc, doctree)
        logger.info('done')

def setup(app):
    app.add_builder(SingleFileTextBuilder)
