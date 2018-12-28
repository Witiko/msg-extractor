import logging
import olefile
from dev_classes.attachment import Attachment
from dev_classes.recipient import Recipient
from extract_msg import constants
from extract_msg.properties import Properties
from extract_msg.utils import encode, has_len, stri, windowsUnicode



logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class Message(olefile.OleFileIO):
    """
    Developer version of the `extract_msg.message.Message` class.
    """
    def __init__(self, path, prefix=''):
        """
        :param path: path to the msg file in the system or is the raw msg file.
        :param prefix: used for extracting embeded msg files
            inside the main one. Do not set manually unless
            you know what you are doing.
        :param attachmentClass: optional, the class the Message object
            will use for attachments. You probably should
            not change this value unless you know what you
            are doing.
        :param filename: optional, the filename to be used by default when saving.
        """
        logger.debug('prefix: {}'.format(prefix))
        self.__path = path
        olefile.OleFileIO.__init__(self, path)
        prefixl = []
        if prefix != '':
            if not isinstance(prefix, stri):
                try:
                    prefix = '/'.join(prefix)
                except:
                    raise TypeError('Invalid prefix type: ' + str(type(prefix)) +
                        '\n(This was probably caused by you setting it manually).')
            prefix = prefix.replace('\\', '/')
            g = prefix.split("/")
            if g[-1] == '':
                g.pop()
            prefixl = g
            if prefix[-1] != '/':
                prefix += '/'
            filename = self._getStringStream(prefixl[:-1] + ['__substg1.0_3001'], prefix=False)
        self.__prefix = prefix
        self.__prefixList = prefixl

        if filename != None:
            self.filename = filename
        elif has_len(path):
            if len(path) < 1536:
                self.filename = path
            else:
                self.filename = None
        else:
            self.filename = None

        self.mainProperties
        recipientDirs = []

        for dir_ in self.listDir():
            if dir_[len(self.__prefixList)].startswith('__recip') and dir_[
                len(self.__prefixList)] not in recipientDirs:
                recipientDirs.append(dir_[len(self.__prefixList)])

        for recipientDir in recipientDirs:
            Properties(msg._getStream(self.__dir + '/__properties_version1.0'), constants.TYPE_RECIPIENT)
        self.attachments
        self.date

    def listDir(self, streams=True, storages=False):
        """
        Replacement for OleFileIO.listdir that runs at the current prefix directory.
        """
        temp = self.listdir(streams, storages)
        if self.__prefix == '':
            return temp
        prefix = self.__prefix.split('/')
        if prefix[-1] == '':
            prefix.pop()
        out = []
        for x in temp:
            good = True
            if len(x) <= len(prefix):
                good = False
            if good:
                for y in range(len(prefix)):
                    if x[y] != prefix[y]:
                        good = False
            if good:
                out.append(x)
        return out

    def Exists(self, inp):
        """
        Checks if :param inp: exists in the msg file.
        """
        if isinstance(inp, list):
            inp = self.__prefixList + inp
        else:
            inp = self.__prefix + inp
        return self.exists(inp)

    def _getStream(self, filename, prefix=True):
        if isinstance(filename, list):
            filename = '/'.join(filename)
        if prefix:
            filename = self.__prefix + filename
        if self.exists(filename):
            stream = self.openstream(filename)
            return stream.read()
        else:
            logger.info('Stream "{}" was requested but could not be found. Returning `None`.'.format(filename))
            return None

    def _getStringStream(self, filename, prefer='unicode', prefix=True):
        """
        Gets a string representation of the requested filename.
        Checks for both ASCII and Unicode representations and returns
        a value if possible.  If there are both ASCII and Unicode
        versions, then :param prefer: specifies which will be
        returned.
        """

        if isinstance(filename, list):
            # Join with slashes to make it easier to append the type
            filename = '/'.join(filename)

        asciiVersion = self._getStream(filename + '001E', prefix)
        unicodeVersion = windowsUnicode(self._getStream(filename + '001F', prefix))
        if debug._debug:
            # DEBUG
            logger.debug('_getStringSteam called for {}. Ascii version found: {}. Unicode version found: {}.'.format(
                filename, asciiVersion != None, unicodeVersion != None))
        if asciiVersion is None:
            return unicodeVersion
        elif unicodeVersion is None:
            return asciiVersion
        else:
            if prefer == 'unicode':
                return unicodeVersion
            else:
                return asciiVersion

    @property
    def mainProperties(self):
        """
        Returns the Properties instance used by the Message instance.
        """
        try:
            return self._prop
        except AttributeError:
            self._prop = Properties(self._getStream('__properties_version1.0'),
                                    constants.TYPE_MESSAGE if self.__prefix == '' else constants.TYPE_MESSAGE_EMBED)
            return self._prop

    @property
    def date(self):
        """
        Returns the send date, if it exists.
        """
        try:
            return self._date
        except AttributeError:
            self._date = self._prop.date
            return self._date

    @property
    def attachments(self):
        """
        Returns a list of all attachments.
        """
        try:
            return self._attachments
        except AttributeError:
            # Get the attachments
            attachmentDirs = []

            for dir_ in self.listDir():
                if dir_[len(self.__prefixList)].startswith('__attach') and dir_[
                    len(self.__prefixList)] not in attachmentDirs:
                    attachmentDirs.append(dir_[len(self.__prefixList)])

            self._attachments = []

            for attachmentDir in attachmentDirs:
                self._attachments.append(self.__attachmentClass(self, attachmentDir))

            return self._attachments

    @property
    def recipients(self):
        """
        Returns a list of all recipients.
        """
        try:
            return self._recipients
        except AttributeError:
            # Get the recipients
            recipientDirs = []

            for dir_ in self.listDir():
                if dir_[len(self.__prefixList)].startswith('__recip') and dir_[
                    len(self.__prefixList)] not in recipientDirs:
                    recipientDirs.append(dir_[len(self.__prefixList)])

            self._recipients = []

            for recipientDir in recipientDirs:
                Properties(msg._getStream(self.__dir + '/__properties_version1.0'), constants.TYPE_RECIPIENT)

            return self._recipients
