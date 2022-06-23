import enum

from typing import Set


class AddressBookType(enum.Enum):
    """
    The type of object that an address book entry ID represents. MUST be one of
    these or it is invalid.
    """
    LOCAL_MAIL_USER = 0x000
    DISTRIBUTION_LIST = 0x001
    BULLETIN_BOARD_OR_PUBLIC_FOLDER = 0x002
    AUTOMATED_MAILBOX = 0x003
    ORGANIZATIONAL_MAILBOX = 0x004
    PRIVATE_DISTRIBUTION_LIST = 0x005
    REMOTE_MAIL_USER = 0x006
    CONTAINER = 0x100
    TEMPLATE = 0x101
    ONE_OFF_USER = 0x102
    SEARCH = 0x200

class AttachErrorBehavior(enum.Enum):
    """
    The behavior to follow when handling an error in an attachment.
    THROW: Throw the exception regardless of type.
    NOT_IMPLEMENTED: Silence the exception for NotImplementedError.
    BROKEN: Silence the exception for NotImplementedError and for broken
        attachments.
    """
    THROW = 0
    NOT_IMPLEMENTED = 1
    BROKEN = 2

class AttachmentType(enum.Enum):
    """
    The type represented by the attachment.
    """
    DATA = 0
    MSG = 1
    WEB = 2
    SIGNED = 3

class BCImageAlignment(enum.Enum):
    STRETCH = 0x00
    TOP_LEFT = 0x01
    TOP_CENTER = 0x02
    TOP_RIGHT = 0x03
    MIDDLE_LEFT = 0x04
    MIDDLE_CENTER = 0x05
    MIDDLE_RIGHT = 0x06
    BOTTOM_LEFT = 0x07
    BOTTOM_CENTER = 0x08
    BOTTOM_RIGHT = 0x09

class BCImageSource(enum.Enum):
    CONTACT_PHOTO = 0
    CARD_PHOTO = 1

class BCLabelFormat(enum.Enum):
    """
    The format for a label of a business card. Left of the underscore represents
    the alignment, right indicates reading order.
    A
    """
    NO_LABEL = 0b000
    RIGHT_LTR = 0b001
    LEFT_LTR = 0b010
    UNKNOWN = 0b100
    RIGHT_RTL = 0b101
    LEFT_RTL = 0b110

class BCTemplateID(enum.Enum):
    """
    The template ID for a business card.

    IM_ALIGN_LEFT: The image area will be left aligned, stretching the full
        height of the card vertically; text fields will appear to the right of
        the image area.
    IM_ALIGN_RIGHT: The image area will be right aligned, stretching the full
        height of the card vertically; text fields will appear to the left of
        the image area.
    IM_ALIGN_TOP: The image area will be aligned to the top, stretching the full
        width of the card horizontally; text fields will appear under the image
        area.
    IM_ALIGN_BOTTOM: The image area will be aligned to the bottom, stretching
        the full width of the card horizontally; text fields will appear above
        the image area.
    NO_IMAGE: No image area is included in the card, only text fields are
        included.
    BACKGROUND: The image area will be used as a background for the card,
        stretching the full height and width of the card. Text fields are
        displayed on top of the image area.
    """
    IM_ALIGN_LEFT = 0x00
    IM_ALIGN_RIGHT = 0x01
    IM_ALIGN_TOP = 0x02
    IM_ALIGN_BOTTOM = 0x03
    NO_IMAGE = 0x04
    BACKGROUND = 0x05

class BCTextFormat(enum.Enum):
    """
    Converts the bits of the text format to an understandable enum value.

    Right value is the alignment, with left is the flags. The following flags
    exist and will be in the following order if present:
        U: Underline.
        I: Italics.
        B: Bold.
        M: The text is multiline.
    """
    LEFT = 0b00000000
    LEFT_M = 0b00000001
    LEFT_B = 0b00000010
    LEFT_BM = 0b00000011
    LEFT_I = 0b00000100
    LEFT_IM = 0b00000101
    LEFT_IB = 0b00000110
    LEFT_IBM = 0b00000111
    LEFT_U = 0b00001000
    LEFT_UM = 0b00001001
    LEFT_UB = 0b00001010
    LEFT_UBM = 0b00001011
    LEFT_UI = 0b00001100
    LEFT_UIM = 0b00001101
    LEFT_UIB = 0b00001110
    LEFT_UIBM = 0b00001111
    CENTER = 0b00100000
    CENTER_M = 0b00100001
    CENTER_B = 0b00100010
    CENTER_BM = 0b00100011
    CENTER_I = 0b00100100
    CENTER_IM = 0b00100101
    CENTER_IB = 0b00100110
    CENTER_IBM = 0b00100111
    CENTER_U = 0b00101000
    CENTER_UM = 0b00101001
    CENTER_UB = 0b00101010
    CENTER_UBM = 0b00101011
    CENTER_UI = 0b00101100
    CENTER_UIM = 0b00101101
    CENTER_UIB = 0b00101110
    CENTER_UIBM = 0b00101111
    RIGHT = 0b00010000
    RIGHT_M = 0b00010001
    RIGHT_B = 0b00010010
    RIGHT_BM = 0b00010011
    RIGHT_I = 0b00010100
    RIGHT_IM = 0b00010101
    RIGHT_IB = 0b00010110
    RIGHT_IBM = 0b00010111
    RIGHT_U = 0b00011000
    RIGHT_UM = 0b00011001
    RIGHT_UB = 0b00011010
    RIGHT_UBM = 0b00011011
    RIGHT_UI = 0b00011100
    RIGHT_UIM = 0b00011101
    RIGHT_UIB = 0b00011110
    RIGHT_UIBM = 0b00011111

class ContactAddressIndex(enum.Enum):
    EMAIL_1 = 0
    EMAIL_2 = 1
    EMAIL_3 = 2
    FAX_1 = 3
    FAX_2 = 4
    FAX_3 = 5

class ContactLinkState(enum.Enum):
    """
    Values for PidLidContactLinkGlobalAddressListLinkState.

    DUPLICATE_NOT_LINKED: The duplicate contact is not linked to the GAL contact
        or the GAL contact is not downloaded.
    DUPLICATE_LINKED: The duplicate contact is linked to the GAL contact.
    DUPLICATE_CANNOT_LINK: The duplicate contact cannot be automatically linked
        to the GAL contact.
    """
    DUPLICATE_NOT_LINKED = 0
    DUPLICATE_LINKED = 1
    DUPLICATE_CANNOT_LINK = 2

class DeencapType(enum.Enum):
    """
    Enum to specify to custom deencapsulation functions the type of data being
    requested.
    """
    PLAIN = 0
    HTML = 1

class DisplayType(enum.Enum):
    MAILUSER = 0x0000
    DISTLIST = 0x0001
    FORUM = 0x0002
    AGENT = 0x0003
    ORGANIZATION = 0x0004
    PRIVATE_DISTLIST = 0x0005
    REMOTE_MAILUSER = 0x0006
    CONTAINER = 0x0100
    TEMPLATE = 0x0101
    ADDRESS_TEMPLATE = 0x0102
    SEARCH = 0x0200

class ElectronicAddressProperties(enum.Enum):
    @classmethod
    def fromBits(cls, value : int) -> Set['ElectronicAddressProperties']:
        """
        Converts an int, with the left most bit referring to 0x00000000, to a
        set of this enum.

        :raises ValueError: The value was less than 0.
        """
        if value < 0:
            raise ValueError('Value must not be negative.')
        # This is a quick compressed way to convert the bits in the int into
        # a tuple of instances of this class should any bit be a 1.
        return tuple(cls(int(x)) for index, val in enumerate(bin(value)[:1:-1]) if val == '1')

    EMAIL_1 = 0x00000000
    EMAIL_2 = 0x00000001
    EMAIL_3 = 0x00000002
    BUSINESS_FAX = 0x00000003
    HOME_FAX = 0x00000004
    PRIMARY_FAX = 0x00000005

class EntryIDType(enum.Enum):
    """
    Converts a UID to the type of Entry ID structure.
    """
    def toHex(self):
        """
        Converts an EntryIDType to it's hex equivelent.
        """
        return EntryIDTypeHex[self.name]

    ADDRESS_BOOK_RECIPIENT = b'\xDC\xA7\x40\xC8\xC0\x42\x10\x1A\xB4\xB9\x08\x00\x2B\x2F\xE1\x82'
    # Contact address or personal distribution list recipient.
    CA_OR_PDL_RECIPIENT = b'\xFE\x42\xAA\x0A\x18\xC7\x1A\x10\xE8\x85\x0B\x65\x1C\x24\x00\x00'
    NNTP_NEWSGROUP_FOLDER = b'\x38\xA1\xBB\x10\x05\xE5\x10\x1A\xA1\xBB\x08\x00\x2B\x2A\x56\xC2'
    ONE_OFF_RECIPIENT = b'\x81\x2B\x1F\xA4\xBE\xA3\x10\x19\x9D\x6E\x00\xDD\x01\x0F\x54\x02'
    PERMANENT = b'\xDC\xA7\x40\xC8\xC0\x42\x10\x1A\xB4\xB9\x08\x00\x2B\x2F\xE1\x82'
    PUBLIC_MESSAGE_STORE = b'\x1A\x44\x73\x90\xAA\x66\x11\xCD\x9B\xC8\x00\xAA\x00\x2F\xC4\x5A'
    # [MS-OXOCNTC] WrappedEntryId Structure.
    WRAPPED = b'\xC0\x91\xAD\xD3\x51\x9D\xCF\x11\xA4\xA9\x00\xAA\x00\x47\xFA\xA4'

class EntryIDTypeHex(enum.Enum):
    """
    Converts a UID to the type of Entry ID structure. Uses a hex string instead
    of bytes for the value.
    """
    def toRaw(self):
        """
        Converts and EntryIDTypeHex to it's raw equivelent.
        """
        return EntryIDType[self.name]

    ADDRESS_BOOK_RECIPIENT = 'DCA740C8C042101AB4B908002B2FE182'
    # Contact address or personal distribution list recipient.
    CA_OR_PDL_RECIPIENT = 'FE42AA0A18C71A10E8850B651C240000'
    NNTP_NEWSGROUP_FOLDER = '38A1BB1005E5101AA1BB08002B2A56C2'
    ONE_OFF_RECIPIENT = '812B1FA4BEA310199D6E00DD010F5402'
    PERMANENT = 'DCA740C8C042101AB4B908002B2FE182'
    PUBLIC_MESSAGE_STORE = '1A447390AA6611CD9BC800AA002FC45A'
    # [MS-OXOCNTC] WrappedEntryId Structure.
    WRAPPED = 'C091ADD3519DCF11A4A900AA0047FAA4'

class ErrorCode(enum.Enum):
    SUCCESS = 0x00000000
    GENERAL_FAILURE = 0x80004005
    OUT_OF_MEMORY = 0x8007000E
    INVALID_PARAMETER = 0x80070057
    NO_INTERFACE = 0x80004002
    ACCESS_DENIED = 0x80070005
    STORAGE_INVALID_FUNCTION = 0x80030001
    STORAGE_ACCESS_DENIED = 0x80030005
    STORAGE_INSUFFICIENT_MEMORY = 0x80030008
    STORAGE_INVALID_POINTER = 0x80030009
    STORAGE_READ_FAULT = 0x8003001E
    STORAGE_LOCK_VIOLATION = 0x80030021
    STORAGE_INVALID_PARAMETER = 0x80030057
    STREAM_SIZE_ERROR = 0x80030070
    STORAGE_INVALID_FLAG = 0x800300FF
    STORAGE_CANNOT_SAVE = 0x80030103
    NOT_SUPPORTED = 0x80040102
    INVALID_CHARACTER_WIDTH = 0x80040103
    STRING_TOO_LONG = 0x80040105
    INVALID_FLAG = 0x80040106
    INVALID_ENTRY_ID = 0x80040107
    INVALID_OBJECT = 0x80040108
    OBJECT_CHANGED = 0x80040109
    OBJECT_DELETED = 0x8004010A
    SERVER_BUSY = 0x8004010B
    OUT_OF_DISK = 0x8004010D
    OUT_OF_RESOURCES = 0x8004010E
    NOT_FOUND = 0x8004010F
    VERSION_MISMATCH = 0x80040110
    LOGON_FAILED = 0x80040111
    TOO_MANY_SESSIONS = 0x80040112
    USER_CANCELED = 0x80040113
    ABORT_FAILED = 0x80040114
    NETWORK_ERROR = 0x80040115
    DISK_ERROR = 0x80040116
    TOO_COMPLEX = 0x80040117
    INVALID_COLUMN = 0x80040118
    COMPUTED_VALUE = 0x8004011A
    CORRUPT_DATA = 0x8004011B
    INVALID_CODEPAGE = 0x8004011E
    INVALID_LOCALE = 0x8004011F
    TIME_SKEW = 0x80040123
    END_OF_SESSION = 0x80040200
    UNKNOWN_ENTRY_ID = 0x80040201
    NOT_COMPLETED = 0x80040400
    TIMEOUT = 0x80040401
    EMPTY_TABLE = 0x80040402
    TABLE_TOO_BIG = 0x80040403
    INVALID_BOOKMARK = 0x80040405
    ERROR_WAIT = 0x80040500
    ERROR_CANCEL = 0x80040501
    NO_SUPPRESS = 0x80040602
    COLLIDING_NAMES = 0x80040604
    NOT_INITIALIZED = 0x80040605
    NO_RECIPIENTS = 0x80040607
    ALREADY_SENT = 0x80040608
    HAS_FOLDERS = 0x80040609
    HAS_MESSAGES = 0x8004060A
    FOLDER_CYCLE = 0x8004060B
    TOO_MANY_LOCKS = 0x8004060D
    AMBIGUOUS_RECIPIENT = 0x80040700
    SYNC_OBJECT_DELETED = 0x80040800
    IGNORE_FAILURE = 0x80040801
    SYNC_CONFLICT = 0x80040802
    NO_PARENT_FOLDER = 0x80040803
    CYCLE_DETECTED = 0x80040804
    NOT_SYNCHRONIZED = 0x80040805
    NAMED_PROPERTY_QUOTA = 0x80040900
    NOT_IMPLEMENTED = 0x80040FFF

class ErrorCodeType(enum.Enum):
    """
    Enum representing values for PtypErrorCode.

    See "Additional Error Codes" in [MS-OXCDATA].
    """
    SUCCESS = 0x00000000
    ISAM_ERROR = 0x000003EA
    UNKNOWN_USER = 0x000003EB
    EXITING = 0x000003ED
    BAD_CONFIGURATION = 0x000003EE
    UNKNOWN_CODE_PAGE = 0x000003EF
    SERVER_MEMORY = 0x000003F0
    LOGIN_PERMISSION = 0x000003F2
    DATABASE_ROLLED_BACK = 0x000003F3
    DATABASE_COPIED_ERROR = 0x000003F4
    AUDIT_NOT_ALLOWED = 0x000003F5
    ZOMBIE_USER = 0x000003F6
    UNCONVERTABLE_ACL = 0x000003F7
    NO_FREE_JET_SESSIONS = 0x0000044C
    DIFFERENT_JET_SESSION = 0x0000044D
    FILE_REMOVE = 0x0000044F
    PARAMETER_OVERFLOW = 0x00000450
    BAD_VERSION = 0x00000451
    TOO_MANY_COLUMNS = 0x00000452
    HAVE_MORE = 0x00000453
    DATABASE_ERROR = 0x00000454
    INDEX_NAME_TOO_BIG = 0x00000455
    UNSUPPORTED_PROPERTY = 0x00000456
    MESSAGE_NOT_SAVED = 0x00000457
    UNPUBLISHED_NOTIFICATION = 0x00000459
    DIFFERENT_ROOT = 0x0000045B
    BAD_FOLDER_NAME = 0x0000045C
    ATTACHMENT_OPEN = 0x0000045D
    INVALID_COLLAPSE_STATE = 0x0000045E
    SKIP_MY_CHILDREN = 0x0000045F
    SEARCH_FOLDER = 0x00000460
    NOT_SEARCH_FOLDER = 0x00000461
    FOLDER_SET_RECEIVE = 0x00000462
    NO_RECEIVE_FOLDER = 0x00000463
    DELETE_SUBMITTED_MESSAGE = 0x00000465
    INVALID_RECIPIENTS = 0x00000467
    NO_REPLICA_HERE = 0x00000468
    NO_REPLICA_AVAILABLE = 0x00000469
    PUBLIC_DATABASE = 0x0000046A
    NOT_PUBLIC_DATABASE = 0x0000046B
    RECORD_NOT_FOUND = 0x0000046C
    REPLICATION_CONFLICT = 0x0000046D
    FX_BUFFER_OVERRUN = 0x00000470
    FX_BUFFER_EMPTY = 0x00000471
    FX_PARTIAL_VALUE = 0x00000472
    FX_NO_ROOM = 0x00000473
    TIME_EXPIRED = 0x00000474
    DESTINATION_ERROR = 0x00000475
    DATABASE_NOT_INITIALIZED = 0x00000476
    WRONG_SERVER = 0x00000478
    BUFFER_TOO_SMALL = 0x0000047D
    ATTACHMENT_RESOLUTION_REQUIRED = 0x0000047E
    SERVER_PAUSED = 0x0000047F
    SERVER_BUSY = 0x00000480
    NO_SUCH_LOGON = 0x00000481
    LOAD_LIBRARY_FAILED = 0x00000482
    ALREADY_CONFIGURED = 0x00000483
    NOT_CONFIGURED = 0x00000484
    DATA_LOSS = 0x00000485
    MAXIMUM_SEND_THREAD_EXCEEDED = 0x00000488
    FX_ERROR_MARKER = 0x00000489
    NO_FREE_JTABS = 0x0000048A
    NOT_PRIVATE_DATABASE = 0x0000048B
    ISINTEG_MDB = 0x0000048C
    RECOVERY_MISMATCH = 0x0000048D
    TABLE_MAY_NOT_BE_DELETED = 0x0000048E
    SEARCH_FOLDER_SCOPE_VIOLATION = 0x00000490
    RPC_REGISTER_IF = 0x000004B1
    RPC_LISTEN = 0x000004B2
    RPC_FORMAT = 0x000004B6
    NO_COPY_TO = 0x000004B7
    NULL_OBJECT = 0x000004B9
    RPC_AUTHENTICATION = 0x000004BC
    RPC_BAD_AUTHENTICATION_LEVEL = 0x000004BD
    NULL_COMMENT_RESTRICTION = 0x000004BE
    RULES_LOAD_ERROR = 0x000004CC
    RULES_DELIVER_ERR = 0x000004CD
    RULES_PARSING_ERR = 0x000004CE
    RULES_CREATE_DAE = 0x000004CF
    RULES_CREATE_DAM = 0x000004D0
    RULES_NO_MOVE_COPY_FOLDER = 0x000004D1
    RULES_NO_FOLDER_RIGHTS = 0x000004D2
    MESSAGE_TOO_BIG = 0x000004D4
    FORM_NOT_VALID = 0x000004D5
    NOT_AUTHORIZED = 0x000004D6
    DELETE_MESSAGE = 0x000004D7
    BOUNCE_MESSAGE = 0x000004D8
    QUOTA_EXCEEDED = 0x000004D9
    MAX_SUBMISSION_EXCEEDED = 0x000004DA
    MAX_ATTACHMENT_EXCEEDED = 0x000004DB
    SEND_AS_DENIED = 0x000004DC
    SHUTOFF_QUOTA_EXCEEDED = 0x000004DD
    TOO_MANY_OPEN_OBJECTS = 0x000004DE
    CLIENT_VERSION_BLOCKED = 0x000004DF
    RPC_HTTP_DISALLOWED = 0x000004E0
    CACHED_MODE_REQUIRED = 0x000004E1
    FOLDER_NOT_CLEANED_UP = 0x000004E3
    FORMAT_ERROR = 0x000004ED
    NOT_EXPANDED = 0x000004F7
    NOT_COLLAPSED = 0x000004F8
    NO_EXPAND_LEAF_ROW = 0x000004F9
    UNREGISTERED_NAME_PROP = 0x000004FA
    FOLDER_DISABLED = 0x000004FB
    DOMAIN_ERROR = 0x000004FC
    NO_CREATE_RIGHT = 0x000004FF
    PUBLIC_ROOT = 0x00000500
    NO_READ_RIGHT = 0x00000501
    NO_CREATE_SUBFOLDER_RIGHT = 0x00000502
    MESSAGE_CYCLE = 0x00000504
    NULL_DESTINATION_OBJECT = 0x00000503
    TOO_MANY_RECIPS = 0x00000505
    VIRUS_SCAN_IN_PROGRESS = 0x0000050A
    VIRUS_DETECTED = 0x0000050B
    MAILBOX_IN_TRANSIT = 0x0000050C
    BACKUP_IN_PROGRESS = 0x0000050D
    VIRUS_MESSAGE_DELETED = 0x0000050E
    INVALID_BACKUP_SEQUENCE = 0x0000050F
    INVALID_BACKUP_TYPE = 0x00000510
    TOO_MANY_BACKUPS = 0x00000511
    RESTORE_IN_PROGRESS = 0x00000512
    DUPLICATE_OBJECT = 0x00000579
    OBJECT_NOT_FOUND = 0x0000057A
    FIXUP_REPLY_RULE = 0x0000057B
    TEMPLATE_NOT_FOUND = 0x0000057C
    RULE_EXECUTION = 0x0000057D
    DS_NO_SUCH_OBJECT = 0x0000057E
    ALREADY_TOMBSTONED = 0x0000057F
    READ_ONLY_TRANSACTION = 0x00000596
    PAUSED = 0x0000060E
    NOT_PAUSED = 0x0000060F
    WRONG_MAILBOX = 0x00000648
    CHANGE_PASSWORD = 0x0000064C
    PASSWORD_EXPIRED = 0x0000064D
    INVALID_WORKSTATION = 0x0000064E
    INVALID_LOGON_HOURS = 0x0000064F
    ACCOUNT_DISABLED = 0x00000650
    RULE_VERSION = 0x000006A4
    RULE_FORMAT = 0x000006A5
    RULE_SEND_AS_DENIED = 0x000006A6
    NO_SERVER_SUPPORT = 0x000006B9
    LOCK_TIMED_OUT = 0x000006BA
    OBJECT_LOCKED = 0x000006BB
    INVALID_LOCK_NAMESPACE = 0x000006BD
    MESSAGE_DELETED = 0x000007D6
    PROTOCOL_DISABLED = 0x000007D8
    CLEARTEXT_LOGON_DISABLED = 0x000007D9
    REJECTED = 0x000007EE
    AMBIGUOUS_ALIAS = 0x0000089A
    UNKNOWN_MAILBOX = 0x0000089B
    EXPRESSION_RESERVED = 0x000008FC
    EXPRESSION_PARSE_DEPTH = 0x000008FD
    EXPRESSION_ARGUMENT_TYPE = 0x000008FE
    EXPRESSION_SYNTAX = 0x000008FF
    EXPRESSION_BAD_STRING_TOKEN = 0x00000900
    EXPRESSION_BAD_COL_TOKEN = 0x00000901
    EXPRESSION_TYPE_MISMATCH = 0x00000902
    EXPRESSION_OPERATOR_NOT_SUPPORTED = 0x00000903
    EXPRESSION_DIVIDE_BY_ZERO = 0x00000904
    EXPRESSION_UNARY_ARGUMENT = 0x00000905
    NOT_LOCKED = 0x00000960
    CLIENT_EVENT = 0x00000961
    CORRUPT_EVENT = 0x00000965
    CORRUPT_WATERMARK = 0x00000966
    EVENT_ERROR = 0x00000967
    WATERMARK_ERROR = 0x00000968
    NON_CANONICAL_ACL = 0x00000969
    MAILBOX_DISABLED = 0x0000096C
    RULES_FOLDER_OVER_QUOTA = 0x0000096D
    ADDRESS_BOOK_UNAVAILABLE = 0x0000096E
    ADDRESS_BOOK_ERROR = 0x0000096F
    ADDRESS_BOOK_OBJECT_NOT_FOUND = 0x00000971
    ADDRESS_BOOK_PROPERTY_ERROR = 0x00000972
    NOT_ENCRYPTED = 0x00000970
    RPC_SERVER_TOO_BUSY = 0x00000973
    RPC_OUT_OF_MEMORY = 0x00000974
    RPC_SERVER_OUT_OF_MEMORY = 0x00000975
    RPC_OUT_OF_RESOURCES = 0x00000976
    RPC_SERVER_UNAVAILABLE = 0x00000977
    SECURE_SUBMIT_ERROR = 0x0000097A
    EVENTS_DELETED = 0x0000097C
    SUBSYSTEM_STOPPING = 0x0000097D
    ATTENDANT_UNAVAILABLE = 0x0000097E
    CI_STOPPING = 0x00000A28
    FX_INVALID_STATE = 0x00000A29
    FX_UNEXPECTED_MARKER = 0x00000A2A
    DUPLICATE_DELIVERY = 0x00000A2B
    CONDITION_VIOLATION = 0x00000A2C
    MAXIMUM_CONNECTION_POOLS_EXCEEDED = 0x00000A2D
    INVALID_RPC_HANDLE = 0x00000A2E
    EVENT_NOT_FOUND = 0x00000A2F
    PROPERTY_NOT_PROMOTED = 0x00000A30
    LOW_FREE_SPACE_FOR_DATABASE = 0x00000A31
    LOW_FREE_SPACE_FOR_LOGS = 0x00000A32
    MAILBOX_IS_QUARANTINED = 0x00000A33
    DATABASE_MOUNT_IN_PROGRESS = 0x00000A34
    DATABASE_DISMOUNT_IN_PROGRESS = 0x00000A35
    CONNECTIONS_OVER_BUDGET = 0x00000A36
    NOT_FOUND_IN_CONTAINER = 0x00000A37
    CANNOT_REMOVE = 0x00000A38
    INVALID_CONNECTION_POOL = 0x00000A39
    VIRUS_SCAN_GENERAL_FAILURE = 0x00000A3A
    ISAM_ERROR_RFS_FAILURE = 0xFFFFFF9C
    ISAM_ERROR_RFS_NOT_ARMED = 0xFFFFFF9B
    ISAM_ERROR_FILE_CLOSE = 0xFFFFFF9A
    ISAM_ERROR_OUT_OF_THREADS = 0xFFFFFF99
    ISAM_ERROR_TOO_MANY_IO = 0xFFFFFF97
    ISAM_ERROR_TASK_DROPPED = 0xFFFFFF96
    ISAM_ERROR_INTERNAL_ERROR = 0xFFFFFF95
    ISAM_ERROR_DATABASE_BUFFER_DEPENDENCIES_CORRUPTED = 0xFFFFFF01
    ISAM_ERROR_PREVIOUS_VERSION = 0xFFFFFEBE
    ISAM_ERROR_PAGE_BOUNDARY = 0xFFFFFEBD
    ISAM_ERROR_KEY_BOUNDARY = 0xFFFFFEBC
    ISAM_ERROR_BAD_PAGE_LINK = 0xFFFFFEB9
    ISAM_ERROR_BAD_BOOKMARK = 0xFFFFFEB8
    ISAM_ERROR_NT_SYSTEM_CALL_FAILED = 0xFFFFFEB2
    ISAM_ERROR_BAD_PARENT_PAGE_LINK = 0xFFFFFEAE
    ISAM_ERROR_SP_AVAIL_EXT_CACHE_OUT_OF_SYNC = 0xFFFFFEAC
    ISAM_ERROR_SP_AVAIL_EXT_CORRUPTED = 0xFFFFFEAB
    ISAM_ERROR_SP_AVAIL_EXT_CACHE_OUT_OF_MEMORY = 0xFFFFFEAA
    ISAM_ERROR_SP_OWN_EXT_CORRUPTED = 0xFFFFFEA9
    ISAM_ERROR_DB_TIME_CORRUPTED = 0xFFFFFEA8
    ISAM_ERROR_KEY_TRUNCATED = 0xFFFFFEA6
    ISAM_ERROR_KEY_TOO_BIG = 0xFFFFFE68
    ISAM_ERROR_INVALID_LOGGED_OPERATION = 0xFFFFFE0C
    ISAM_ERROR_LOG_FILE_CORRUPT = 0xFFFFFE0B
    ISAM_ERROR_NO_BACKUP_DIRECTORY = 0xFFFFFE09
    ISAM_ERROR_BACKUP_DIRECTORY_NOT_EMPTY = 0xFFFFFE08
    ISAM_ERROR_BACKUP_IN_PROGRESS = 0xFFFFFE07
    ISAM_ERROR_RESTORE_IN_PROGRESS = 0xFFFFFE06
    ISAM_ERROR_MISSING_PREVIOUS_LOG_FILE = 0xFFFFFE03
    ISAM_ERROR_LOG_WRITE_FAIL = 0xFFFFFE02
    ISAM_ERROR_LOG_DISABLED_DUE_TO_RECOVERY_FAILURE = 0xFFFFFE01
    ISAM_ERROR_CANNOT_LOG_DURING_RECOVERY_REDO = 0xFFFFFE00
    ISAM_ERROR_LOG_GENERATION_MISMATCH = 0xFFFFFDFF
    ISAM_ERROR_BAD_LOG_VERSION = 0xFFFFFDFE
    ISAM_ERROR_INVALID_LOG_SEQUENCE = 0xFFFFFDFD
    ISAM_ERROR_LOGGING_DISABLED = 0xFFFFFDFC
    ISAM_ERROR_LOG_BUFFER_TOO_SMALL = 0xFFFFFDFB
    ISAM_ERROR_LOG_SEQUENCE_END = 0xFFFFFDF9
    ISAM_ERROR_NO_BACKUP = 0xFFFFFDF8
    ISAM_ERROR_INVALID_BACKUP_SEQUENCE = 0xFFFFFDF7
    ISAM_ERROR_BACKUP_NOT_ALLOWED_YET = 0xFFFFFDF5
    ISAM_ERROR_DELETE_BACKUP_FILE_FAIL = 0xFFFFFDF4
    ISAM_ERROR_MAKE_BACKUP_DIRECTORY_FAIL = 0xFFFFFDF3
    ISAM_ERROR_INVALID_BACKUP = 0xFFFFFDF2
    ISAM_ERROR_RECOVERED_WITH_ERRORS = 0xFFFFFDF1
    ISAM_ERROR_MISSING_LOG_FILE = 0xFFFFFDF0
    ISAM_ERROR_LOG_DISK_FULL = 0xFFFFFDEF
    ISAM_ERROR_BAD_LOG_SIGNATURE = 0xFFFFFDEE
    ISAM_ERROR_BAD_DB_SIGNATURE = 0xFFFFFDED
    ISAM_ERROR_BAD_CHECKPOINT_SIGNATURE = 0xFFFFFDEC
    ISAM_ERROR_CHECKPOINT_CORRUPT = 0xFFFFFDEB
    ISAM_ERROR_MISSING_PATCH_PAGE = 0xFFFFFDEA
    ISAM_ERROR_BAD_PATCH_PAGE = 0xFFFFFDE9
    ISAM_ERROR_REDO_ABRUPT_ENDED = 0xFFFFFDE8
    ISAM_ERROR_BAD_SLV_SIGNATURE = 0xFFFFFDE7
    ISAM_ERROR_PATCH_FILE_MISSING = 0xFFFFFDE6
    ISAM_ERROR_DATABASE_LOG_SET_MISMATCH = 0xFFFFFDE5
    ISAM_ERROR_DATABASE_STREAMING_FILE_MISMATCH = 0xFFFFFDE4
    ISAM_ERROR_LOG_FILE_SIZE_MISMATCH = 0xFFFFFDE3
    ISAM_ERROR_CHECKPOINT_FILE_NOT_FOUND = 0xFFFFFDE2
    ISAM_ERROR_REQUIRED_LOG_FILES_MISSING = 0xFFFFFDE1
    ISAM_ERROR_SOFT_RECOVERY_ON_BACKUP_DATABASE = 0xFFFFFDE0
    ISAM_ERROR_LOG_FILE_SIZE_MISMATCH_DATABASES_CONSISTENT = 0xFFFFFDDF
    ISAM_ERROR_LOG_SECTOR_SIZE_MISMATCH = 0xFFFFFDDE
    ISAM_ERROR_LOG_SECTOR_SIZE_MISMATCH_DATABASES_CONSISTENT = 0xFFFFFDDD
    ISAM_ERROR_LOG_SEQUENCE_END_DATABASES_CONSISTENT = 0xFFFFFDDC
    ISAM_ERROR_STREAMING_DATA_NOT_LOGGED = 0xFFFFFDDB
    ISAM_ERROR_DATABASE_DIRTY_SHUTDOWN = 0xFFFFFDDA
    ISAM_ERROR_CONSISTENT_TIME_MISMATCH = 0xFFFFFDD9
    ISAM_ERROR_DATABASE_PATCH_FILE_MISMATCH = 0xFFFFFDD8
    ISAM_ERROR_ENDING_RESTORE_LOG_TOO_LOW = 0xFFFFFDD7
    ISAM_ERROR_STARTING_RESTORE_LOG_TOO_HIGH = 0xFFFFFDD6
    ISAM_ERROR_GIVEN_LOG_FILE_HAS_BAD_SIGNATURE = 0xFFFFFDD5
    ISAM_ERROR_GIVEN_LOG_FILE_IS_NOT_CONTIGUOUS = 0xFFFFFDD4
    ISAM_ERROR_MISSING_RESTORE_LOG_FILES = 0xFFFFFDD3
    ISAM_ERROR_MISSING_FULL_BACKUP = 0xFFFFFDD0
    ISAM_ERROR_BAD_BACKUP_DATABASE_SIZE = 0xFFFFFDCF
    ISAM_ERROR_DATABASE_ALREADY_UPGRADED = 0xFFFFFDCE
    ISAM_ERROR_DATABASE_INCOMPLETE_UPGRADE = 0xFFFFFDCD
    ISAM_ERROR_MISSING_CURRENT_LOG_FILES = 0xFFFFFDCB
    ISAM_ERROR_DB_TIME_TOO_OLD = 0xFFFFFDCA
    ISAM_ERROR_DB_TIME_TOO_NEW = 0xFFFFFDC9
    ISAM_ERROR_MISSING_FILE_TO_BACKUP = 0xFFFFFDC7
    ISAM_ERROR_LOG_TORN_WRITE_DURING_HARD_RESTORE = 0xFFFFFDC6
    ISAM_ERROR_LOG_TORN_WRITE_DURING_HARD_RECOVERY = 0xFFFFFDC5
    ISAM_ERROR_LOG_CORRUPT_DURING_HARD_RESTORE = 0xFFFFFDC3
    ISAM_ERROR_LOG_CORRUPT_DURING_HARD_RECOVERY = 0xFFFFFDC2
    ISAM_ERROR_MUST_DISABLE_LOGGING_FOR_DB_UPGRADE = 0xFFFFFDC1
    ISAM_ERROR_BAD_RESTORE_TARGET_INSTANCE = 0xFFFFFDBF
    ISAM_ERROR_RECOVERED_WITHOUT_UNDO = 0xFFFFFDBD
    ISAM_ERROR_DATABASES_NOT_FROM_SAME_SNAPSHOT = 0xFFFFFDBC
    ISAM_ERROR_SOFT_RECOVERY_ON_SNAPSHOT = 0xFFFFFDBB
    ISAM_ERROR_COMMITTED_LOG_FILES_MISSING = 0xFFFFFDBA
    ISAM_ERROR_COMMITTED_LOG_FILES_CORRUPT = 0xFFFFFDB6
    ISAM_ERROR_UNICODE_TRANSLATION_BUFFER_TOO_SMALL = 0xFFFFFDA7
    ISAM_ERROR_UNICODE_TRANSLATION_FAIL = 0xFFFFFDA6
    ISAM_ERROR_UNICODE_NORMALIZATION_NOT_SUPPORTED = 0xFFFFFDA5
    ISAM_ERROR_EXISTING_LOG_FILE_HAS_BAD_SIGNATURE = 0xFFFFFD9E
    ISAM_ERROR_EXISTING_LOG_FILE_IS_NOT_CONTIGUOUS = 0xFFFFFD9D
    ISAM_ERROR_LOG_READ_VERIFY_FAILURE = 0xFFFFFD9C
    ISAM_ERROR_SLV_READ_VERIFY_FAILURE = 0xFFFFFD9B
    ISAM_ERROR_CHECKPOINT_DEPTH_TOO_DEEP = 0xFFFFFD9A
    ISAM_ERROR_RESTORE_OF_NON_BACKUP_DATABASE = 0xFFFFFD99
    ISAM_ERROR_INVALID_GRBIT = 0xFFFFFC7C
    ISAM_ERROR_TERM_IN_PROGRESS = 0xFFFFFC18
    ISAM_ERROR_FEATURE_NOT_AVAILABLE = 0xFFFFFC17
    ISAM_ERROR_INVALID_NAME = 0xFFFFFC16
    ISAM_ERROR_INVALID_PARAMETER = 0xFFFFFC15
    ISAM_ERROR_DATABASE_FILE_READ_ONLY = 0xFFFFFC10
    ISAM_ERROR_INVALID_DATABASE_ID = 0xFFFFFC0E
    ISAM_ERROR_OUT_OF_MEMORY = 0xFFFFFC0D
    ISAM_ERROR_OUT_OF_DATABASE_SPACE = 0xFFFFFC0C
    ISAM_ERROR_OUT_OF_CURSORS = 0xFFFFFC0B
    ISAM_ERROR_OUT_OF_BUFFERS = 0xFFFFFC0A
    ISAM_ERROR_TOO_MANY_INDEXES = 0xFFFFFC09
    ISAM_ERROR_TOO_MANY_KEYS = 0xFFFFFC08
    ISAM_ERROR_RECORD_DELETED = 0xFFFFFC07
    ISAM_ERROR_READ_VERIFY_FAILURE = 0xFFFFFC06
    ISAM_ERROR_PAGE_NOT_INITIALIZED = 0xFFFFFC05
    ISAM_ERROR_OUT_OF_FILE_HANDLES = 0xFFFFFC04
    ISAM_ERROR_DISK_IO = 0xFFFFFC02
    ISAM_ERROR_INVALID_PATH = 0xFFFFFC01
    ISAM_ERROR_INVALID_SYSTEM_PATH = 0xFFFFFC00
    ISAM_ERROR_INVALID_LOG_DIRECTORY = 0xFFFFFBFF
    ISAM_ERROR_RECORD_TOO_BIG = 0xFFFFFBFE
    ISAM_ERROR_TOO_MANY_OPEN_DATABASES = 0xFFFFFBFD
    ISAM_ERROR_INVALID_DATABASE = 0xFFFFFBFC
    ISAM_ERROR_NOT_INITIALIZED = 0xFFFFFBFB
    ISAM_ERROR_ALREADY_INITIALIZED = 0xFFFFFBFA
    ISAM_ERROR_INIT_IN_PROGRESS = 0xFFFFFBF9
    ISAM_ERROR_FILE_ACCESS_DENIED = 0xFFFFFBF8
    ISAM_ERROR_BUFFER_TOO_SMALL = 0xFFFFFBF2
    ISAM_ERROR_TOO_MANY_COLUMNS = 0xFFFFFBF0
    ISAM_ERROR_CONTAINER_NOT_EMPTY = 0xFFFFFBED
    ISAM_ERROR_INVALID_FILENAME = 0xFFFFFBEC
    ISAM_ERROR_INVALID_BOOKMARK = 0xFFFFFBEB
    ISAM_ERROR_COLUMN_IN_USE = 0xFFFFFBEA
    ISAM_ERROR_INVALID_BUFFER_SIZE = 0xFFFFFBE9
    ISAM_ERROR_COLUMN_NOT_UPDATABLE = 0xFFFFFBE8
    ISAM_ERROR_INDEX_IN_USE = 0xFFFFFBE5
    ISAM_ERROR_LINK_NOT_SUPPORTED = 0xFFFFFBE4
    ISAM_ERROR_NULL_KEY_DISALLOWED = 0xFFFFFBE3
    ISAM_ERROR_NOT_IN_TRANSACTION = 0xFFFFFBE2
    ISAM_ERROR_TOO_MANY_ACTIVE_USERS = 0xFFFFFBDD
    ISAM_ERROR_INVALID_COUNTRY = 0xFFFFFBDB
    ISAM_ERROR_INVALID_LANGUAGE_ID = 0xFFFFFBDA
    ISAM_ERROR_INVALID_CODE_PAGE = 0xFFFFFBD9
    ISAM_ERROR_INVALID_LC_MAP_STRING_FLAGS = 0xFFFFFBD8
    ISAM_ERROR_VERSION_STORE_ENTRY_TOO_BIG = 0xFFFFFBD7
    ISAM_ERROR_VERSION_STORE_OUT_OF_MEMORY_AND_CLEANUP_TIMED_OUT = 0xFFFFFBD6
    ISAM_ERROR_VERSION_STORE_OUT_OF_MEMORY = 0xFFFFFBD3
    ISAM_ERROR_CANNOT_INDEX = 0xFFFFFBD1
    ISAM_ERROR_RECORD_NOT_DELETED = 0xFFFFFBD0
    ISAM_ERROR_TOO_MANY_MEMPOOL_ENTRIES = 0xFFFFFBCF
    ISAM_ERROR_OUT_OF_OBJECT_I_DS = 0xFFFFFBCE
    ISAM_ERROR_OUT_OF_LONG_VALUE_I_DS = 0xFFFFFBCD
    ISAM_ERROR_OUT_OF_AUTOINCREMENT_VALUES = 0xFFFFFBCC
    ISAM_ERROR_OUT_OF_DBTIME_VALUES = 0xFFFFFBCB
    ISAM_ERROR_OUT_OF_SEQUENTIAL_INDEX_VALUES = 0xFFFFFBCA
    ISAM_ERROR_RUNNING_IN_ONE_INSTANCE_MODE = 0xFFFFFBC8
    ISAM_ERROR_RUNNING_IN_MULTI_INSTANCE_MODE = 0xFFFFFBC7
    ISAM_ERROR_SYSTEM_PARAMS_ALREADY_SET = 0xFFFFFBC6
    ISAM_ERROR_SYSTEM_PATH_IN_USE = 0xFFFFFBC5
    ISAM_ERROR_LOG_FILE_PATH_IN_USE = 0xFFFFFBC4
    ISAM_ERROR_TEMP_PATH_IN_USE = 0xFFFFFBC3
    ISAM_ERROR_INSTANCE_NAME_IN_USE = 0xFFFFFBC2
    ISAM_ERROR_INSTANCE_UNAVAILABLE = 0xFFFFFBBE
    ISAM_ERROR_DATABASE_UNAVAILABLE = 0xFFFFFBBD
    ISAM_ERROR_INSTANCE_UNAVAILABLE_DUE_TO_FATAL_LOG_DISK_FULL = 0xFFFFFBBC
    ISAM_ERROR_OUT_OF_SESSIONS = 0xFFFFFBB3
    ISAM_ERROR_WRITE_CONFLICT = 0xFFFFFBB2
    ISAM_ERROR_TRANS_TOO_DEEP = 0xFFFFFBB1
    ISAM_ERROR_INVALID_SESID = 0xFFFFFBB0
    ISAM_ERROR_WRITE_CONFLICT_PRIMARY_INDEX = 0xFFFFFBAF
    ISAM_ERROR_IN_TRANSACTION = 0xFFFFFBAC
    ISAM_ERROR_ROLLBACK_REQUIRED = 0xFFFFFBAB
    ISAM_ERROR_TRANS_READ_ONLY = 0xFFFFFBAA
    ISAM_ERROR_SESSION_WRITE_CONFLICT = 0xFFFFFBA9
    ISAM_ERROR_RECORD_TOO_BIG_FOR_BACKWARD_COMPATIBILITY = 0xFFFFFBA8
    ISAM_ERROR_CANNOT_MATERIALIZE_FORWARD_ONLY_SORT = 0xFFFFFBA7
    ISAM_ERROR_SESID_TABLE_ID_MISMATCH = 0xFFFFFBA6
    ISAM_ERROR_INVALID_INSTANCE = 0xFFFFFBA5
    ISAM_ERROR_DATABASE_DUPLICATE = 0xFFFFFB4F
    ISAM_ERROR_DATABASE_IN_USE = 0xFFFFFB4E
    ISAM_ERROR_DATABASE_NOT_FOUND = 0xFFFFFB4D
    ISAM_ERROR_DATABASE_INVALID_NAME = 0xFFFFFB4C
    ISAM_ERROR_DATABASE_INVALID_PAGES = 0xFFFFFB4B
    ISAM_ERROR_DATABASE_CORRUPTED = 0xFFFFFB4A
    ISAM_ERROR_DATABASE_LOCKED = 0xFFFFFB49
    ISAM_ERROR_CANNOT_DISABLE_VERSIONING = 0xFFFFFB48
    ISAM_ERROR_INVALID_DATABASE_VERSION = 0xFFFFFB47
    ISAM_ERROR_DATABASE200_FORMAT = 0xFFFFFB46
    ISAM_ERROR_DATABASE400_FORMAT = 0xFFFFFB45
    ISAM_ERROR_DATABASE500_FORMAT = 0xFFFFFB44
    ISAM_ERROR_PAGE_SIZE_MISMATCH = 0xFFFFFB43
    ISAM_ERROR_TOO_MANY_INSTANCES = 0xFFFFFB42
    ISAM_ERROR_DATABASE_SHARING_VIOLATION = 0xFFFFFB41
    ISAM_ERROR_ATTACHED_DATABASE_MISMATCH = 0xFFFFFB40
    ISAM_ERROR_DATABASE_INVALID_PATH = 0xFFFFFB3F
    ISAM_ERROR_DATABASE_ID_IN_USE = 0xFFFFFB3E
    ISAM_ERROR_FORCE_DETACH_NOT_ALLOWED = 0xFFFFFB3D
    ISAM_ERROR_CATALOG_CORRUPTED = 0xFFFFFB3C
    ISAM_ERROR_PARTIALLY_ATTACHED_DB = 0xFFFFFB3B
    ISAM_ERROR_DATABASE_SIGN_IN_USE = 0xFFFFFB3A
    ISAM_ERROR_DATABASE_CORRUPTED_NO_REPAIR = 0xFFFFFB38
    ISAM_ERROR_INVALID_CREATE_DB_VERSION = 0xFFFFFB37
    ISAM_ERROR_TABLE_LOCKED = 0xFFFFFAEA
    ISAM_ERROR_TABLE_DUPLICATE = 0xFFFFFAE9
    ISAM_ERROR_TABLE_IN_USE = 0xFFFFFAE8
    ISAM_ERROR_OBJECT_NOT_FOUND = 0xFFFFFAE7
    ISAM_ERROR_DENSITY_INVALID = 0xFFFFFAE5
    ISAM_ERROR_TABLE_NOT_EMPTY = 0xFFFFFAE4
    ISAM_ERROR_INVALID_TABLE_ID = 0xFFFFFAE2
    ISAM_ERROR_TOO_MANY_OPEN_TABLES = 0xFFFFFAE1
    ISAM_ERROR_ILLEGAL_OPERATION = 0xFFFFFAE0
    ISAM_ERROR_TOO_MANY_OPEN_TABLES_AND_CLEANUP_TIMED_OUT = 0xFFFFFADF
    ISAM_ERROR_OBJECT_DUPLICATE = 0xFFFFFADE
    ISAM_ERROR_INVALID_OBJECT = 0xFFFFFADC
    ISAM_ERROR_CANNOT_DELETE_TEMP_TABLE = 0xFFFFFADB
    ISAM_ERROR_CANNOT_DELETE_SYSTEM_TABLE = 0xFFFFFADA
    ISAM_ERROR_CANNOT_DELETE_TEMPLATE_TABLE = 0xFFFFFAD9
    ISAM_ERROR_EXCLUSIVE_TABLE_LOCK_REQUIRED = 0xFFFFFAD6
    ISAM_ERROR_FIXED_DDL = 0xFFFFFAD5
    ISAM_ERROR_FIXED_INHERITED_DDL = 0xFFFFFAD4
    ISAM_ERROR_CANNOT_NEST_DDL = 0xFFFFFAD3
    ISAM_ERROR_DDL_NOT_INHERITABLE = 0xFFFFFAD2
    ISAM_ERROR_INVALID_SETTINGS = 0xFFFFFAD0
    ISAM_ERROR_CLIENT_REQUEST_TO_STOP_JET_SERVICE = 0xFFFFFACF
    ISAM_ERROR_CANNOT_ADD_FIXED_VAR_COLUMN_TO_DERIVED_TABLE = 0xFFFFFACE
    ISAM_ERROR_INDEX_CANT_BUILD = 0xFFFFFA87
    ISAM_ERROR_INDEX_HAS_PRIMARY = 0xFFFFFA86
    ISAM_ERROR_INDEX_DUPLICATE = 0xFFFFFA85
    ISAM_ERROR_INDEX_NOT_FOUND = 0xFFFFFA84
    ISAM_ERROR_INDEX_MUST_STAY = 0xFFFFFA83
    ISAM_ERROR_INDEX_INVALID_DEF = 0xFFFFFA82
    ISAM_ERROR_INVALID_CREATE_INDEX = 0xFFFFFA7F
    ISAM_ERROR_TOO_MANY_OPEN_INDEXES = 0xFFFFFA7E
    ISAM_ERROR_MULTI_VALUED_INDEX_VIOLATION = 0xFFFFFA7D
    ISAM_ERROR_INDEX_BUILD_CORRUPTED = 0xFFFFFA7C
    ISAM_ERROR_PRIMARY_INDEX_CORRUPTED = 0xFFFFFA7B
    ISAM_ERROR_SECONDARY_INDEX_CORRUPTED = 0xFFFFFA7A
    ISAM_ERROR_INVALID_INDEX_ID = 0xFFFFFA78
    ISAM_ERROR_INDEX_TUPLES_SECONDARY_INDEX_ONLY = 0xFFFFFA6A
    ISAM_ERROR_INDEX_TUPLES_TOO_MANY_COLUMNS = 0xFFFFFA69
    ISAM_ERROR_INDEX_TUPLES_NON_UNIQUE_ONLY = 0xFFFFFA68
    ISAM_ERROR_INDEX_TUPLES_TEXT_BINARY_COLUMNS_ONLY = 0xFFFFFA67
    ISAM_ERROR_INDEX_TUPLES_VAR_SEG_MAC_NOT_ALLOWED = 0xFFFFFA66
    ISAM_ERROR_INDEX_TUPLES_INVALID_LIMITS = 0xFFFFFA65
    ISAM_ERROR_INDEX_TUPLES_CANNOT_RETRIEVE_FROM_INDEX = 0xFFFFFA64
    ISAM_ERROR_INDEX_TUPLES_KEY_TOO_SMALL = 0xFFFFFA63
    ISAM_ERROR_COLUMN_LONG = 0xFFFFFA23
    ISAM_ERROR_COLUMN_NO_CHUNK = 0xFFFFFA22
    ISAM_ERROR_COLUMN_DOES_NOT_FIT = 0xFFFFFA21
    ISAM_ERROR_NULL_INVALID = 0xFFFFFA20
    ISAM_ERROR_COLUMN_INDEXED = 0xFFFFFA1F
    ISAM_ERROR_COLUMN_TOO_BIG = 0xFFFFFA1E
    ISAM_ERROR_COLUMN_NOT_FOUND = 0xFFFFFA1D
    ISAM_ERROR_COLUMN_DUPLICATE = 0xFFFFFA1C
    ISAM_ERROR_MULTI_VALUED_COLUMN_MUST_BE_TAGGED = 0xFFFFFA1B
    ISAM_ERROR_COLUMN_REDUNDANT = 0xFFFFFA1A
    ISAM_ERROR_INVALID_COLUMN_TYPE = 0xFFFFFA19
    ISAM_ERROR_TAGGED_NOT_NULL = 0xFFFFFA16
    ISAM_ERROR_NO_CURRENT_INDEX = 0xFFFFFA15
    ISAM_ERROR_KEY_IS_MADE = 0xFFFFFA14
    ISAM_ERROR_BAD_COLUMN_ID = 0xFFFFFA13
    ISAM_ERROR_BAD_ITAG_SEQUENCE = 0xFFFFFA12
    ISAM_ERROR_COLUMN_IN_RELATIONSHIP = 0xFFFFFA11
    ISAM_ERROR_CANNOT_BE_TAGGED = 0xFFFFFA0F
    ISAM_ERROR_DEFAULT_VALUE_TOO_BIG = 0xFFFFFA0C
    ISAM_ERROR_MULTI_VALUED_DUPLICATE = 0xFFFFFA0B
    ISAM_ERROR_LV_CORRUPTED = 0xFFFFFA0A
    ISAM_ERROR_MULTI_VALUED_DUPLICATE_AFTER_TRUNCATION = 0xFFFFFA08
    ISAM_ERROR_DERIVED_COLUMN_CORRUPTION = 0xFFFFFA07
    ISAM_ERROR_INVALID_PLACEHOLDER_COLUMN = 0xFFFFFA06
    ISAM_ERROR_RECORD_NOT_FOUND = 0xFFFFF9BF
    ISAM_ERROR_RECORD_NO_COPY = 0xFFFFF9BE
    ISAM_ERROR_NO_CURRENT_RECORD = 0xFFFFF9BD
    ISAM_ERROR_RECORD_PRIMARY_CHANGED = 0xFFFFF9BC
    ISAM_ERROR_KEY_DUPLICATE = 0xFFFFF9BB
    ISAM_ERROR_ALREADY_PREPARED = 0xFFFFF9B9
    ISAM_ERROR_KEY_NOT_MADE = 0xFFFFF9B8
    ISAM_ERROR_UPDATE_NOT_PREPARED = 0xFFFFF9B7
    ISAM_ERROR_DATA_HAS_CHANGED = 0xFFFFF9B5
    ISAM_ERROR_LANGUAGE_NOT_SUPPORTED = 0xFFFFF9AD
    ISAM_ERROR_TOO_MANY_SORTS = 0xFFFFF95B
    ISAM_ERROR_INVALID_ON_SORT = 0xFFFFF95A
    ISAM_ERROR_TEMP_FILE_OPEN_ERROR = 0xFFFFF8F5
    ISAM_ERROR_TOO_MANY_ATTACHED_DATABASES = 0xFFFFF8F3
    ISAM_ERROR_DISK_FULL = 0xFFFFF8F0
    ISAM_ERROR_PERMISSION_DENIED = 0xFFFFF8EF
    ISAM_ERROR_FILE_NOT_FOUND = 0xFFFFF8ED
    ISAM_ERROR_FILE_INVALID_TYPE = 0xFFFFF8EC
    ISAM_ERROR_AFTER_INITIALIZATION = 0xFFFFF8C6
    ISAM_ERROR_LOG_CORRUPTED = 0xFFFFF8C4
    ISAM_ERROR_INVALID_OPERATION = 0xFFFFF88E
    ISAM_ERROR_ACCESS_DENIED = 0xFFFFF88D
    ISAM_ERROR_TOO_MANY_SPLITS = 0xFFFFF88B
    ISAM_ERROR_SESSION_SHARING_VIOLATION = 0xFFFFF88A
    ISAM_ERROR_ENTRY_POINT_NOT_FOUND = 0xFFFFF889
    ISAM_ERROR_SESSION_CONTEXT_ALREADY_SET = 0xFFFFF888
    ISAM_ERROR_SESSION_CONTEXT_NOT_SET_BY_THIS_THREAD = 0xFFFFF887
    ISAM_ERROR_SESSION_IN_USE = 0xFFFFF886
    ISAM_ERROR_RECORD_FORMAT_CONVERSION_FAILED = 0xFFFFF885
    ISAM_ERROR_ONE_DATABASE_PER_SESSION = 0xFFFFF884
    ISAM_ERROR_ROLLBACK_ERROR = 0xFFFFF883
    ISAM_ERROR_CALLBACK_FAILED = 0xFFFFF7CB
    ISAM_ERROR_CALLBACK_NOT_RESOLVED = 0xFFFFF7CA
    ISAM_ERROR_OS_SNAPSHOT_INVALID_SEQUENCE = 0xFFFFF69F
    ISAM_ERROR_OS_SNAPSHOT_TIME_OUT = 0xFFFFF69E
    ISAM_ERROR_OS_SNAPSHOT_NOT_ALLOWED = 0xFFFFF69D
    ISAM_ERROR_OS_SNAPSHOT_INVALID_SNAP_ID = 0xFFFFF69C
    ISAM_ERROR_LS_CALLBACK_NOT_SPECIFIED = 0xFFFFF448
    ISAM_ERROR_LS_ALREADY_SET = 0xFFFFF447
    ISAM_ERROR_LS_NOT_SET = 0xFFFFF446
    ISAM_ERROR_FILE_IO_SPARSE = 0xFFFFF060
    ISAM_ERROR_FILE_IO_BEYOND_EOF = 0xFFFFF05F
    ISAM_ERROR_FILE_COMPRESSED = 0xFFFFF05B

class Gender(enum.Enum):
    # Seems rather binary, which is less than ideal. We are directly using the
    # terms used by the documentation.
    UNSPECIFIED = 0x0000
    FEMALE = 0x0001
    MALE = 0x0002

class Guid(enum.Enum):
    PS_MAPI = '{00020328-0000-0000-C000-000000000046}'
    PS_PUBLIC_STRINGS = '{00020329-0000-0000-C000-000000000046}'
    PSETID_COMMON = '{00062008-0000-0000-C000-000000000046}'
    PSETID_ADDRESS = '{00062004-0000-0000-C000-000000000046}'
    PS_INTERNET_HEADERS = '{00020386-0000-0000-C000-000000000046}'
    PSETID_APPOINTMENT = '{00062002-0000-0000-C000-000000000046}'
    PSETID_MEETING = '{6ED8DA90-450B-101B-98DA-00AA003F1305}'
    PSETID_LOG = '{0006200A-0000-0000-C000-000000000046}'
    PSETID_MESSAGING = '{41F28F13-83F4-4114-A584-EEDB5A6B0BFF}'
    PSETID_NOTE = '{0006200E-0000-0000-C000-000000000046}'
    PSETID_POSTRSS = '{00062041-0000-0000-C000-000000000046}'
    PSETID_TASK = '{00062003-0000-0000-C000-000000000046}'
    PSETID_UNIFIEDMESSAGING = '{4442858E-A9E3-4E80-B900-317A210CC15B}'
    PSETID_AIRSYNC = '{71035549-0739-4DCB-9163-00F0580DBBDF}'
    PSETID_SHARING = '{00062040-0000-0000-C000-000000000046}'
    PSETID_XMLEXTRACTEDENTITIES = '{23239608-685D-4732-9C55-4C95CB4E8E33}'
    PSETID_ATTACHMENT = '{96357F7F-59E1-47D0-99A7-46515C183B54}'

class Importance(enum.Enum):
    LOW = 0
    MEDIUM = 1
    IMPORTANCE_HIGH = 2

class Intelligence(enum.Enum):
    DUMB = 0
    SMART = 1

class MacintoshEncoding(enum.Enum):
    """
    The encoding to use for Macintosh-specific data attachments.
    """
    BIN_HEX = 0
    UUENCODE = 1
    APPLE_SINGLE = 2
    APPLE_DOUBLE = 3

class MessageFormat(enum.Enum):
    TNEF = 0
    MIME = 1

class MessageType(enum.Enum):
    PRIVATE_FOLDER = 0x0001
    PUBLIC_FOLDER = 0x0003
    MAPPED_PUBLIC_FOLDER = 0x0005
    PRIVATE_MESSAGE = 0x0007
    PUBLIC_MESSAGE = 0x0009
    MAPPED_PUBLIC_MESSAGE = 0x000B
    PUBLIC_NEWSGROUP_FOLDER = 0x000C

class NamedPropertyType(enum.Enum):
    NUMERICAL_NAMED = 0
    STRING_NAMED = 1

class OORBodyFormat(enum.Enum):
    """
    The body format for One Off Recipients.
    """
    TEXT_ONLY = 0b0011
    HTML_ONLY = 0b0111
    TEXT_AND_HTML = 0b1011
    # This one isn't actually listed in the documentation, but I've seen it and
    # this is my best guess for what a format of `0` is meant to mean. This will
    # also prevent the code from failing on a 0 format.
    UNSPECIFIED = 0b0000

class PostalAddressID(enum.Enum):
    UNSPECIFIED = 0x00000000
    HOME = 0x00000001
    WORK = 0x00000002
    OTHER = 0x00000003

class Priority(enum.Enum):
    URGENT = 0x00000001
    NORMAL = 0x00000000
    NOT_URGENT = 0xFFFFFFFF

class PropertiesType(enum.Enum):
    """
    The type of the properties instance.
    """
    MESSAGE = 0
    MESSAGE_EMBED = 1
    ATTACHMENT = 2
    RECIPIENT = 3

class RecipientRowFlagType(enum.Enum):
    NOTYPE = 0x0
    X500DN = 0x1
    MSMAIL = 0x2
    SMTP = 0x3
    FAX = 0x4
    PROFESSIONALOFFICESYSTEM = 0x5
    PERSONALDESTRIBUTIONLIST1 = 0x6
    PERSONALDESTRIBUTIONLIST2 = 0x7

class RecipientType(enum.Enum):
    """
    The type of recipient.
    """
    SENDER = 0
    TO = 1
    CC = 2
    BCC = 3

class RuleActionType(enum.Enum):
    OP_MOVE = 0x01
    OP_COPY = 0x02
    OP_REPLY = 0x03
    OP_OOF_REPLY = 0x04
    OP_DEFER_ACTION = 0x05
    OP_BOUNCE = 0x06
    OP_FORWARD = 0x07
    OP_DELEGATE = 0x08
    OP_TAG = 0x09
    OP_DELETE = 0x0A
    OP_MARK_AS_READ = 0x0B

class Sensitivity(enum.Enum):
    NORMAL = 0
    PERSONAL = 1
    PRIVATE = 2
    CONFIDENTIAL = 3

class TaskAcceptance(enum.Enum):
    """
    The acceptance state of the task.
    """
    NOT_ASSIGNED = 0x00000000
    UNKNOWN = 0x00000001
    ACCEPTED = 0x00000002
    REJECTED = 0x00000003

class TaskHistory(enum.Enum):
    """
    The type of the last change to the Task object.
    """
    NONE = 0x00000000
    ACCEPTED = 0x00000001
    REJECTED = 0x00000002
    OTHER = 0x00000003
    DUE_DATE_CHANGED = 0x00000004
    ASSIGNED = 0x00000005

class TaskMode(enum.Enum):
    """
    The mode of the Task object used in task communication (PidLidTaskMode).

    UNASSIGNED: The Task object is not assigned.
    EMBEDDED_REQUEST: The Task object is embedded in a task request.
    ACCEPTED: The Task object has been accepted by the task assignee.
    REJECTED: The Task object was rejected by the task assignee.
    EMBEDDED_UPDATE: The Task object is embedded in a task update.
    SELF_ASSIGNED: The Task object was assigned to the task assigner
        (self-delegation).
    """
    UNASSIGNED = 0
    EMBEDDED_REQUEST = 1
    ACCEPTED = 2
    REJECTED = 3
    EMBEDDED_UPDATE = 4
    SELF_ASSIGNED = 5

class TaskOwnership(enum.Enum):
    """
    The role of the current user relative to the Task object.

    NOT_ASSIGNED: The Task object is not assigned.
    ASSIGNERS_COPY: The Task object is the task assigner's copy of the Task
        object.
    ASSIGNEES_COPY: The Task object is the task assignee's copy of the Task
        object.
    """
    NOT_ASSIGNED = 0x00000000
    ASSIGNERS_COPY = 0x00000001
    ASSIGNEES_COPY = 0x00000002

class TaskStatus(enum.Enum):
    """
    The status of a task object (PidLidTaskStatus).

    NOT_STARTED: The user has not started the task.
    IN_PROGRESS: The users's work on the Task object is in progress.
    COMPLETE: The user's work on the Task object is complete.
    WAITING_ON_OTHER: The user is waiting on somebody else.
    DEFERRED: The user has deffered work on the Task object.
    """
    NOT_STARTED = 0x00000000
    IN_PROGRESS = 0x00000001
    COMPLETE = 0x00000002
    WAITING_ON_OTHER = 0x00000003
    DEFERRED = 0x00000004
