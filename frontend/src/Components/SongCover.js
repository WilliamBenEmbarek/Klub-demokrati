import React from 'react';
import './SongCover.css'

class SongCover extends React.Component {
    handleClick = () => {
        this.props.onVote(this.props.songId);
    }

    render() {
        return(
                // eslint-disable-next-line
                <div className="SongCover" onClick={() => this.handleClick()}><img class="AlbumArt" src={this.props.image}/>
                    <div className='songText'>{this.props.songName} - {this.props.artist}: Votes {this.props.votes}</div>
                </div>
        );
    }
}
export default SongCover;