import torch
from torch.cuda.amp import autocast as autocast


def seq_inference(vid, vid_lgt, model, device):
    model.eval()

    vid = device.data_to_device(vid)
    vid_lgt = device.data_to_device(vid_lgt)
    with torch.no_grad():
        ret_dict = model(vid, vid_lgt, label=None, label_lgt=None)
    total_sent = ret_dict['recognized_sents']

    del vid
    del vid_lgt

    return total_sent


def write2file(path, info, output):
    filereader = open(path, "w")
    for sample_idx, sample in enumerate(output):
        for word_idx, word in enumerate(sample):
            filereader.writelines(
                "{} 1 {:.2f} {:.2f} {}\n".format(info[sample_idx],
                                                 word_idx * 1.0 / 100,
                                                 (word_idx + 1) * 1.0 / 100,
                                                 word[0]))
